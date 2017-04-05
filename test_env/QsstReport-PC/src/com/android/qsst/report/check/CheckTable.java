package com.android.qsst.report.check;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JTable;
import javax.swing.table.TableCellRenderer;
import javax.swing.table.TableColumn;


public class CheckTable extends JTable implements MouseListener {
    private static final long serialVersionUID = 584842405181279389L;

    private final int DEFAULT_CHECKHEADERCOLUMN = -1;

    private final int DEFAULT_PREFERREDWIDTH = 23;

    private final int DEFAULT_MAXWIDTH = 23;

    private final int DEFAULT_MINWIDTH = 23;

    private int checkHeaderColumn = DEFAULT_CHECKHEADERCOLUMN;

    private final HeaderCheckBoxRenderer checkHeader = new HeaderCheckBoxRenderer();

    private TableCellRenderer oldCheckHeader = null;

    private boolean oldEnable = false;
    private ICheckedListener checkedListener = null;

    /*
     * (non-Javadoc)
     * @see java.awt.event.MouseListener#mouseClicked(java.awt.event.MouseEvent)
     */
    @Override
    public void mouseClicked(MouseEvent e) {
//        if (this.columnAtPoint(e.getPoint()) != this.checkHeaderColumn) {
//            return;
//        }

        if(e.getButton() == MouseEvent.BUTTON3) {
            return;
        }
        if (e.getSource() == this.getTableHeader()) {
            if (this.columnAtPoint(e.getPoint()) != this.checkHeaderColumn) {
                return;
            }
            boolean isSelected = !checkHeader.isSelected();
            checkHeader.setSelected(isSelected);
            this.getTableHeader().repaint();
            checkColumnCells(isSelected);
        } else {
            int row = this.rowAtPoint(e.getPoint());
            boolean isSelected = !(Boolean) (this.getModel().getValueAt(row, this.checkHeaderColumn));
            this.getModel().setValueAt(isSelected, row, this.checkHeaderColumn);
            notificationCheckStatusChanged(row, isSelected);
            checkColumnHeader();
        }
    }

    /*
     * (non-Javadoc)
     * @see java.awt.event.MouseListener#mouseEntered(java.awt.event.MouseEvent)
     */
    @Override
    public void mouseEntered(MouseEvent e) {
    }

    /*
     * (non-Javadoc)
     * @see java.awt.event.MouseListener#mouseExited(java.awt.event.MouseEvent)
     */
    @Override
    public void mouseExited(MouseEvent e) {
    }

    /*
     * (non-Javadoc)
     * @see java.awt.event.MouseListener#mousePressed(java.awt.event.MouseEvent)
     */
    @Override
    public void mousePressed(MouseEvent e) {
    }

    /*
     * (non-Javadoc)
     * @see java.awt.event.MouseListener#mouseReleased(java.awt.event.MouseEvent)
     */
    @Override
    public void mouseReleased(MouseEvent e) {
    }

    public int getCheckHeaderColumn() {
        return checkHeaderColumn;
    }

    public void setCheckHeaderColumn(int checkHeaderColumn) {
        TableColumn tableColumn;

        if (isCheckHeader()) {
            tableColumn = this.getColumnModel().getColumn(this.checkHeaderColumn);

            if (null != oldCheckHeader) {
                tableColumn.setHeaderRenderer(oldCheckHeader);
                this.setEnabled(oldEnable);
            }

            this.getTableHeader().removeMouseListener(this);
            this.removeMouseListener(this);
        }

        this.checkHeaderColumn = checkHeaderColumn;

        if (!isCheckHeader()) {
            this.checkHeaderColumn = DEFAULT_CHECKHEADERCOLUMN;
            return;
        }

        tableColumn = this.getColumnModel().getColumn(this.checkHeaderColumn);
        tableColumn.setPreferredWidth(DEFAULT_PREFERREDWIDTH);
        tableColumn.setMaxWidth(DEFAULT_MAXWIDTH);
        tableColumn.setMinWidth(DEFAULT_MINWIDTH);
        oldCheckHeader = tableColumn.getHeaderRenderer();
        tableColumn.setHeaderRenderer(checkHeader);
        this.getTableHeader().addMouseListener(this);
        this.addMouseListener(this);
        oldEnable = this.isEnabled();

        if (oldEnable) {
            this.setEnabled(false);
        }

        checkColumnHeader();
    }

    public void checkColumnCells(boolean isCheck) {
        if (!isCheckHeader()) {
            return;
        }

        for (int ii = 0; ii < this.getRowCount(); ii++) {
            this.getModel().setValueAt(isCheck, ii, this.checkHeaderColumn);
            notificationCheckStatusChanged(ii, isCheck);
        }
    }

    public void checkColumnHeader() {
        if (hasCheckedRow()) {
            if (this.checkHeader.isSelected()) {
                return;
            }

            this.checkHeader.setSelected(true);
            this.getTableHeader().repaint();
        } else {
            if (!this.checkHeader.isSelected()) {
                return;
            }

            this.checkHeader.setSelected(false);
            this.getTableHeader().repaint();
        }
    }

    public boolean isCheckHeader() {
        return !(this.checkHeaderColumn < 0 || this.checkHeaderColumn >= this.getColumnCount());
    }

    public boolean hasCheckedRow() {
        if (!isCheckHeader()) {
            return false;
        }

        for (int ii = 0; ii < this.getRowCount(); ii++) {
            boolean isCheck = (Boolean) this.getModel().getValueAt(ii, this.checkHeaderColumn);

            if (isCheck) {
                return true;
            }
        }

        return false;
    }

    public List <Integer> getAllCheckedRows() {
        List <Integer> rows = new ArrayList <Integer>();

        if (!isCheckHeader()) {
            return rows;
        }

        for (int ii = 0; ii < this.getRowCount(); ii++) {
            boolean isCheck = (Boolean) this.getModel().getValueAt(ii, this.checkHeaderColumn);

            if (isCheck) {
                rows.add(ii);
            }
        }

        return rows;
    }

    public List <Object> getAllCheckedColumn(int col) {
        List <Object> rows = new ArrayList <Object>();

        if (!isCheckHeader()) {
            return rows;
        }

        for (int ii = 0; ii < this.getRowCount(); ii++) {
            boolean isCheck = (Boolean) this.getModel().getValueAt(ii, this.checkHeaderColumn);

            if (isCheck) {
                rows.add(this.getModel().getValueAt(ii, col));
            }
        }

        return rows;
    }
    public void setCheckedListener(ICheckedListener l) {
        checkedListener = l;
    }
    private void notificationCheckStatusChanged(int row, boolean isChecked) {
        if(checkedListener!=null) {
            checkedListener.onStatusChanged(row, isChecked);
        }
    }
}
