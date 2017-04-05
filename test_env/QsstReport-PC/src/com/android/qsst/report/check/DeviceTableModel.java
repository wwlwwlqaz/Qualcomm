package com.android.qsst.report.check;

import java.util.ArrayList;
import java.util.List;

import com.android.qsst.report.check.bean.DeviceBean;

public class DeviceTableModel extends CheckTableModel {
    private static final long serialVersionUID = 2901808435846952546L;
    private String[] mColumnNames = null;
    private List<DeviceBean> mCheckBeans = null;

    public DeviceTableModel() {
        this(null,null);
    }
    public DeviceTableModel(String[] columnNames) {
        this(columnNames, null);
    }
    public DeviceTableModel(String[] columnNames, List<DeviceBean> beans) {
        super();
        mColumnNames = columnNames;
        mCheckBeans = beans;
    }

    public void setDeviceBeans(List<DeviceBean> beans) throws Exception {
        mCheckBeans = beans;
    }

    @Override
    public String[] getColumns() {
        return mColumnNames;
    }

    @Override
    public Object fillColumns(int row, int col) {
        DeviceBean deviceBean= mCheckBeans.get(row);
        if(col ==0 ) {
            return deviceBean.isCheck();
        } else if (col == 1){
            return deviceBean.getSn();
        } else {
            return deviceBean.getStatus();
        }
    }

    @Override
    public void setColumns(int row, int col, Object newValue) {
        DeviceBean deviceBean= mCheckBeans.get(row);
        if(col ==0 ) {
            deviceBean.setCheck((Boolean) newValue);
        } else {
            //fileBean.setFileName((String)newValue);
        }
    }

    @Override
    public int getCheckBeanCount() {
            return mCheckBeans == null ? 0 : mCheckBeans.size();
    }
    public List<DeviceBean> getSelectedDevices() {
        if(mCheckBeans==null) {
            return null;
        }
        List<DeviceBean> selectDevices = new ArrayList<DeviceBean>();
        for(DeviceBean deviceBean:mCheckBeans) {
            if(deviceBean.isCheck()) {
                selectDevices.add(deviceBean);
            }
        }
        return selectDevices;
    }
}
