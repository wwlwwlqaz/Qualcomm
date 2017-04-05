import system_capacity

def query_capacity():
    if system_capacity.get_property("persist.multisim.config").strip() == "ssss":
        return "com.qsst.ssss"
    return None
