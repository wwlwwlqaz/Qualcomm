package com.android.qsst.report;

import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.File;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.ScrollPaneConstants;
import javax.swing.table.TableCellRenderer;
import javax.swing.table.TableColumn;

import com.android.qsst.report.check.CheckTable;
import com.android.qsst.report.check.DeviceTableModel;
import com.android.qsst.report.check.bean.DeviceBean;
import com.android.qsst.report.config.ConfigFactory;
import com.android.qsst.report.config.Workspace;
import com.android.qsst.report.device.Commands;
import com.android.qsst.report.device.DeviceFactory;
import com.android.qsst.report.device.JavaExecuteCommand;
import com.android.qsst.report.util.ReportUtils;

public class DevicePane extends JSplitPane implements ActionListener,INotification{
    private static final long serialVersionUID = 1L;
    private static final String BUTTON_CMD_EXECUTE = "EXECUTE";

    private QsstReport mQsstReport = null;
    private JPanel  mConfigPane = null;
    private JPanel  mRightPane = null;
    private JCheckBox mClearLogging = null;
    private JButton mExecute = null;
    private JLabel  mMessageLabel = null;

    private JScrollPane mFilesPane = null;
    private JScrollPane mOperationPane = null;
    private CheckTable mDeviceTable = null;
    private DeviceTableModel mDeviceTableModel = null;
    private String[] mColumnNames = new String[] {
            "Check",
            "SN",
            "Status"
            };
    private List<DeviceBean> mDevices = null;
    private Timer mTimer = null;

    public DevicePane(QsstReport qsstReport) {
        setOrientation(JSplitPane.HORIZONTAL_SPLIT);
        setResizeWeight(0.5);
        setOneTouchExpandable(true);
        mQsstReport = qsstReport;
        int width = mQsstReport.getAppWidth();
        int minHeight = 200;//mQsstReport.getAppHeight();

        mDeviceTableModel = new DeviceTableModel(mColumnNames);
        mDeviceTable = new CheckTable();
        mDeviceTable.setModel(mDeviceTableModel);
        mDeviceTable.setCheckHeaderColumn(0);
        mDeviceTable.setEnabled(true);
        mDeviceTable.setRowHeight(30);
        mDeviceTable.setBorder(BorderFactory.createEtchedBorder());
        mDeviceTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        mDeviceTable.getTableHeader().setReorderingAllowed(false);
        mDeviceTable.setShowGrid(false);
        mDeviceTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        mDeviceTable.setDefaultRenderer(Object.class, new FileTableRenderer());
        mDeviceTable.setVisible(true);

        refreshTable();

        mConfigPane = new JPanel(null);
        mConfigPane.setBounds(20, 10, 240, 70);
        mConfigPane.setBorder(BorderFactory.createTitledBorder("Cofniguration"));

        mClearLogging = new JCheckBox("clear up the logging workspace");
        mClearLogging.setToolTipText("clear up the logging workspace");
        mClearLogging.setBounds(20, 20, 200, 30);

        mConfigPane.add(mClearLogging);

        mExecute = new JButton("Upload");
        mExecute.setForeground(Color.RED);
        mExecute.setFont(new Font("宋体", Font.BOLD, 15));
        mExecute.setBounds(20, (mConfigPane.getSize().height + 20), 150, 30);
        mExecute.setActionCommand(BUTTON_CMD_EXECUTE);
        mExecute.setToolTipText("upload logging to pc");
        mExecute.addActionListener(this);

        //show a message label
        mMessageLabel = new JLabel();
        mMessageLabel.setHorizontalAlignment(JLabel.CENTER);
        mMessageLabel.setForeground(Color.RED);
        mMessageLabel.setVisible(false);
        mMessageLabel.setBounds(20, mExecute.getLocation().y+20, mConfigPane.getSize().width, 25);

        mRightPane = new JPanel(null);
        // mainPanel.setBounds(0, 0, detailPanel.getSize().width, 120);
        mRightPane.setPreferredSize(new Dimension(mConfigPane.getSize().width, 145));
        mRightPane.setAutoscrolls(true);
        mRightPane.add(mConfigPane);
        mRightPane.add(mExecute);
        mRightPane.add(mMessageLabel);

        mFilesPane = new JScrollPane(mDeviceTable,ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        mFilesPane.setMinimumSize(new Dimension(width/3, minHeight));
        mOperationPane = new JScrollPane(mRightPane);
        mOperationPane.setMinimumSize(new Dimension(260, minHeight));
        setLeftComponent(mFilesPane);
        setRightComponent(mOperationPane);
        addPropertyChangeListener(new PropertyChangeListener() {
            public void propertyChange(PropertyChangeEvent evt) {
                if (evt.getPropertyName().equals(JSplitPane.DIVIDER_LOCATION_PROPERTY)) {
                    resizeComponent(Integer.parseInt(evt.getNewValue().toString()));
                }
            }
        });
    }

    public void resizeComponent(int newValue){
        System.out.println("LeftWidth:"+newValue);
        TableColumn column2 = mDeviceTable.getColumn(mColumnNames[2]);
        column2.setPreferredWidth(60);
        TableColumn column1 = mDeviceTable.getColumn(mColumnNames[1]);
        JScrollBar scrollBar = mFilesPane.getVerticalScrollBar();
        int newWidth = newValue-mDeviceTable.getColumn(mColumnNames[0]).getWidth()-2;
        if(scrollBar.isShowing()) {
            newWidth = newWidth - scrollBar.getWidth();
        }
        newWidth = newWidth - column2.getPreferredWidth();
        column1.setPreferredWidth(newWidth);

        int rightWidth = getWidth() - newValue;
        System.out.println("right:"+rightWidth);
//        mConfigPane.setPreferredSize(new Dimension(rightWidth-20, (int)mConfigPane.getPreferredSize().getHeight()));

        mConfigPane.setBounds(20, 10, rightWidth-40, 70);
        Dimension btnDimension = mExecute.getSize();
        mExecute.setBounds((rightWidth-btnDimension.width)/2, (mConfigPane.getSize().height + 20), 150, 30);
        mMessageLabel.setBounds(20, mExecute.getLocation().y+mExecute.getHeight()+5, rightWidth-40, 25);
    }

    public void refreshTable() {
        try {
            List<DeviceBean> selectDevices =mDeviceTableModel.getSelectedDevices();
            mDevices = DeviceFactory.getDevices();
            for(DeviceBean deviceBean:mDevices) {
                boolean isCheck = isChecked(selectDevices, deviceBean.getSn());
                deviceBean.setCheck(isCheck);
            }
            mDeviceTableModel.setDeviceBeans(mDevices);
            mDeviceTable.updateUI();
            mDeviceTable.checkColumnHeader();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private boolean isChecked(List<DeviceBean> selectDevices, String sn) {
        if(selectDevices==null) {
            return false;
        }
        for(DeviceBean deviceBean: selectDevices) {
            if(deviceBean.getSn().equals(sn)) {
                return true;
            }
        }
        return false;
    }

    private void showMessage(String msg){
        mMessageLabel.setVisible(true);
        mMessageLabel.setText(msg);
        mQsstReport.addLogging(msg);

        if(mTimer!=null) {
            mTimer.cancel();
            mTimer = null;
        }
        mTimer = new Timer("Display");
        mTimer.schedule(new TimerTask() {
            @Override
            public void run() {
                mMessageLabel.setText("");
                mMessageLabel.setVisible(false);
            }
        }, 5000);
    }

    public void setUploading(boolean status) {
        mExecute.setEnabled(!status);
        mClearLogging.setEnabled(!status);
        if(status) {
            mExecute.setText("Uploading");
        } else{
            mExecute.setText("Upload");
        }
    }

    @Override
    public void actionPerformed(ActionEvent event) {
        String comm = event.getActionCommand();
        if(BUTTON_CMD_EXECUTE.endsWith(comm)) {
            List<DeviceBean> selectedDevices = mDeviceTableModel.getSelectedDevices();
            if(selectedDevices.size() > 0) {
                new UploadLoggingThread(selectedDevices).start();
            } else {
                showMessage("Please select a device firstly");
            }
        }
    }

    @Override
    public void refresh(Object object) {
        setUploading(false);
        showMessage(null);
    }

    class FileTableRenderer implements TableCellRenderer {
        @Override
        public Component getTableCellRendererComponent(JTable table,
                Object value, boolean isSelected, boolean hasFocus, int row,
                int column) {
            if (column == 0) {
                Boolean isCheck = (Boolean) table.getValueAt(row, column);
                JCheckBox checkbox = new JCheckBox();
                checkbox.setSelected(isCheck);
                return checkbox;
            }
            JLabel label = new JLabel();
            label.setFont(new Font(table.getFont().toString(), Font.BOLD, 14));
            label.setText(value.toString());
            label.setVisible(true);
            label.setOpaque(true);
            return label;
        }

    }
    class UploadLoggingThread extends Thread {
        List<DeviceBean> selectedDevices = null;
        public UploadLoggingThread(List<DeviceBean> selectedDevices) {
            this.selectedDevices =selectedDevices;
        }
        @Override
        public void run() {
            setUploading(true);
            String loggingPath  =getLoggingOnPc();
            if(ReportUtils.isEmpty(loggingPath)) {
                setUploading(false);
                return;
            }
            for(DeviceBean deviceBean:selectedDevices) {
                String sn = deviceBean.getSn();
                mQsstReport.addLogging("Begin upload:"+sn);
                String out = getLoggingPath(sn);
                if(!ReportUtils.isEmpty(out)) {
                    String pullCommand = Commands.ADB_SHELL_PULL.replace("[SN]", sn);
                    pullCommand = pullCommand.replace("[arg1]", out);
                    pullCommand = pullCommand.replace("[arg2]", loggingPath);
                    String[] results = JavaExecuteCommand.getInstance().executeCommand(pullCommand);
                    if(ReportUtils.isEmpty(results[0])) {
                        mQsstReport.addLogging(results[1]);
                    }
                    if(ReportUtils.isEmpty(results[1])) {
                        mQsstReport.addLogging(results[0]);
                    }
                } else {
                    mQsstReport.addLogging("Can not get the device["+sn+"] logging path");
                }
            }
            setUploading(false);
        }

        private String getLoggingOnPc() {
            Workspace wrokspace = ConfigFactory.getInstance().getLoggingWorkspace();
            String  loggingPath = null;
            if(wrokspace == null || ReportUtils.isEmpty(loggingPath = wrokspace.getLoggingDir()) || !new File(loggingPath).exists()) {
                showMessage("Sorry , Please select a available logging workspace.");
                showInitDialog("Please select a available logging workspace.");
                return null;
            } else {
                return wrokspace.getLoggingDir();
            }
        }

        private void showInitDialog(String message) {
            (new InitDialog(mQsstReport, DevicePane.this,message)).setVisible(true);
        }

        private String getLoggingPath(String sn) {
            String loggingCommand = Commands.ADB_SHELL_LOGGING_PATH.replace("[SN]", sn);
            String result = JavaExecuteCommand.getInstance().executeCommand(loggingCommand)[1];
            String[] lines = result.split("\n");
            if(lines!=null && lines.length > 0) {
                for(String line: lines) {
                    int index = line.indexOf(":");
                    int lengthLen = line.length();
                    if(index > 0 && index !=(lengthLen-1) ) {
                        String prefix = line.substring(0, index);
                        String remain = line.substring(index+1, lengthLen);
                        if("LOGGING_PATH".equals(prefix)) {
                            return remain;
                        }
                    }
                }
            }
            return null;
        }
    }
}
