import system_capacity

def query_capacity():
    if system_capacity.get_property("persist.multisim.config").strip() == "dsds":
        return "com.qsst.dsds"
    return None