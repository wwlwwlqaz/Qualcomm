package com.android.qsst.report.check;

import javax.swing.table.AbstractTableModel;

public abstract class CheckTableModel extends AbstractTableModel {

    private static final long serialVersionUID = -1264704523326656387L;

    public CheckTableModel() {

    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.AbstractTableModel#isCellEditable(int, int)
     */
    public boolean isCellEditable(int row, int col) {
        return super.isCellEditable(row, col);
    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.AbstractTableModel#setValueAt(java.lang.Object, int, int)
     */
    public void setValueAt(Object value, int row, int col) {
        setColumns(row, col, value);
        this.fireTableCellUpdated(row, col);
    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.AbstractTableModel#getColumnClass(int)
     */
//    public Class <?> getColumnClass(int column) {
//        Object value = getValueAt(0, column);
//
//        if (value != null) {
//            return value.getClass();
//        }
//
//        return super.getClass();
//    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.TableModel#getColumnCount()
     */
    @Override
    public int getColumnCount() {
        return getColumns().length;
    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.TableModel#getRowCount()
     */
    @Override
    public int getRowCount() {
        return getCheckBeanCount();
    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.TableModel#getValueAt(int, int)
     */
    @Override
    public Object getValueAt(int row, int col) {
        return fillColumns(row, col);
    }

    /*
     * (non-Javadoc)
     * @see javax.swing.table.AbstractTableModel#getColumnName(int)
     */
    public String getColumnName(int col) {
        return getColumns()[col];
    }

    public abstract String[] getColumns();
    public abstract Object fillColumns(int row, int col);
    public abstract void setColumns(int row, int col,Object newValue);
    public abstract int getCheckBeanCount();
}
