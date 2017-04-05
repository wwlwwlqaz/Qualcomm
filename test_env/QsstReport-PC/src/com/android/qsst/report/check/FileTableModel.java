package com.android.qsst.report.check;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import com.android.qsst.report.check.bean.FileBean;

public class FileTableModel extends CheckTableModel {
    private static final long serialVersionUID = 2901808435846952546L;

    private String[] mColumnNames = null;
    private List<FileBean> mCheckBeans = null;

    public FileTableModel() {
        this(null,null);
    }
    public FileTableModel(String[] columnNames) {
        this(columnNames, null);
    }
    public FileTableModel(String[] columnNames, List<FileBean> beans) {
        super();
        mColumnNames = columnNames;
        mCheckBeans = beans;
    }

    public void setFileBeans(List<FileBean> beans) throws Exception {
        mCheckBeans = beans;
    }

    @Override
    public String[] getColumns() {
        return mColumnNames;
    }

    @Override
    public Object fillColumns(int row, int col) {
        FileBean fileBean= mCheckBeans.get(row);
        if(col ==0 ) {
            return fileBean.isCheck();
        } else {
            return fileBean.getFile().getName();
        }
    }

    @Override
    public void setColumns(int row, int col, Object newValue) {
        FileBean fileBean= mCheckBeans.get(row);
        if(col ==0 ) {
            fileBean.setCheck((Boolean) newValue);
        } else {
            //fileBean.setFileName((String)newValue);
        }
    }

    @Override
    public int getCheckBeanCount() {
        return mCheckBeans == null ? 0 : mCheckBeans.size();
    }

    public List<File> getSelectedFiles() {
        if(mCheckBeans==null) {
            return null;
        }
        List<File> selectFiles = new ArrayList<File>();
        for(FileBean fileBean:mCheckBeans) {
            if(fileBean.isCheck()) {
                selectFiles.add(fileBean.getFile());
            }
        }
        return selectFiles;
    }
}
