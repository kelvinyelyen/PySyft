# stdlib
from threading import Thread

# syft absolute
from syft.core.node.new.document_store import PartitionSettings
from syft.core.node.new.document_store import QueryKeys
from syft.core.node.new.kv_document_store import KeyValueStorePartition

# relative
from .store_mocks import MockObjectType
from .store_mocks import MockStoreConfig
from .store_mocks import MockSyftObject


def test_kv_store_partition_sanity() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)

    res = store.init_store()
    assert res.is_ok()

    assert hasattr(store, "data")
    assert hasattr(store, "unique_keys")
    assert hasattr(store, "searchable_keys")


def test_kv_store_partition_init_failed() -> None:
    store_config = MockStoreConfig(is_crashed=True)
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)

    res = store.init_store()
    assert res.is_err()


def test_kv_store_partition_set() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    obj = MockSyftObject(data=1)
    res = store.set(obj, ignore_duplicates=False)

    assert res.is_ok()
    assert res.ok() == obj
    assert len(store.all().ok()) == 1

    res = store.set(obj, ignore_duplicates=False)
    assert res.is_err()
    assert len(store.all().ok()) == 1

    res = store.set(obj, ignore_duplicates=True)
    assert res.is_ok()
    assert len(store.all().ok()) == 1

    obj2 = MockSyftObject(data=2)
    res = store.set(obj2, ignore_duplicates=False)
    assert res.is_ok()
    assert res.ok() == obj2
    assert len(store.all().ok()) == 2


def test_kv_store_partition_set_backend_fail() -> None:
    store_config = MockStoreConfig(is_crashed=True)
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    obj = MockSyftObject(data=1)

    res = store.set(obj, ignore_duplicates=False)
    assert res.is_err()


def test_kv_store_partition_delete() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    objs = []
    for v in range(10):
        obj = MockSyftObject(data=v)
        store.set(obj, ignore_duplicates=False)
        objs.append(obj)

    assert len(store.all().ok()) == len(objs)

    # random object
    obj = MockSyftObject(data="bogus")
    key = settings.store_key.with_obj(obj)
    res = store.delete(key)
    assert res.is_err()
    assert len(store.all().ok()) == len(objs)

    # cleanup store
    for idx, v in enumerate(objs):
        key = settings.store_key.with_obj(v)
        res = store.delete(key)
        assert res.is_ok()
        assert len(store.all().ok()) == len(objs) - idx - 1

        res = store.delete(key)
        assert res.is_err()
        assert len(store.all().ok()) == len(objs) - idx - 1

    assert len(store.all().ok()) == 0


def test_kv_store_partition_update() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    # add item
    obj = MockSyftObject(data=1)
    store.set(obj, ignore_duplicates=False)
    assert len(store.all().ok()) == 1

    # fail to update missing keys
    rand_obj = MockSyftObject(data="bogus")
    key = settings.store_key.with_obj(rand_obj)
    res = store.update(key, obj)
    assert res.is_err()

    # update the key multiple times
    for v in range(10):
        key = settings.store_key.with_obj(obj)
        obj_new = MockSyftObject(data=v)

        res = store.update(key, obj_new)
        assert res.is_ok()

        assert len(store.all().ok()) == 1
        assert store.all().ok()[0].id != obj.id
        assert store.all().ok()[0].id == obj_new.id
        assert store.all().ok()[0].data == v

        stored = store.get_all_from_store(QueryKeys(qks=[key]))
        assert stored.ok()[0].data == v


def test_kv_store_partition_set_multithreaded() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()
    execution_ok = True

    def _kv_cbk(tid: int) -> None:
        nonlocal execution_ok
        for idx in range(100):
            obj = MockSyftObject(data=idx)
            res = store.set(obj, ignore_duplicates=False)

            execution_ok &= res.is_ok()
            assert res.is_ok()

    tids = []
    for tid in range(10):
        thread = Thread(target=_kv_cbk, args=(tid,))
        thread.start()

        tids.append(thread)

    for thread in tids:
        thread.join()

    stored = store.all()

    assert execution_ok
    assert len(stored.ok()) == 1000


def test_kv_store_partition_update_multithreaded() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    obj = MockSyftObject(data=0)
    key = settings.store_key.with_obj(obj)
    store.set(obj, ignore_duplicates=False)
    execution_ok = True

    def _kv_cbk(tid: int) -> None:
        nonlocal execution_ok
        for repeat in range(100):
            stored = store.get_all_from_store(QueryKeys(qks=[key]))
            obj = MockSyftObject(data=stored.ok()[0].data + 1)
            res = store.update(key, obj)

            execution_ok &= res.is_ok()
            assert res.is_ok()

    tids = []
    for tid in range(10):
        thread = Thread(target=_kv_cbk, args=(tid,))
        thread.start()

        tids.append(thread)

    for thread in tids:
        thread.join()

    assert execution_ok
    stored = store.get_all_from_store(QueryKeys(qks=[key]))
    assert stored.ok()[0].data == 1000


def test_kv_store_partition_set_delete_multithreaded() -> None:
    store_config = MockStoreConfig()
    settings = PartitionSettings(name="test", object_type=MockObjectType)

    store = KeyValueStorePartition(settings=settings, store_config=store_config)
    store.init_store()

    thread_cnt = 10
    execution_ok = True

    def _kv_cbk(tid: int) -> None:
        nonlocal execution_ok
        for idx in range(100):
            obj = MockSyftObject(data=idx)
            res = store.set(obj, ignore_duplicates=False)

            execution_ok &= res.is_ok()
            assert res.is_ok()

            key = settings.store_key.with_obj(obj)

            res = store.delete(key)
            execution_ok &= res.is_ok()
            assert res.is_ok()

    tids = []
    for tid in range(thread_cnt):
        thread = Thread(target=_kv_cbk, args=(tid,))
        thread.start()

        tids.append(thread)

    for thread in tids:
        thread.join()

    assert execution_ok
    stored = store.all()
    assert len(stored.ok()) == 0
