package com.android.qsst.report;

import java.awt.Color;
import java.awt.Component;
import java.awt.Desktop;
import java.awt.Desktop.Action;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.util.ArrayList;
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
import com.android.qsst.report.check.FileTableModel;
import com.android.qsst.report.check.ICheckedListener;
import com.android.qsst.report.check.bean.FileBean;
import com.android.qsst.report.config.ConfigFactory;
import com.android.qsst.report.config.Workspace;
import com.android.qsst.report.util.ReportUtils;
import com.android.qsst.report.util.Utils;

public class ReportPane extends JSplitPane implements ActionListener,INotification, ICheckedListener{
    private static final long serialVersionUID = 1L;
    private static final String BUTTON_CMD_EXECUTE = "EXECUTE";

    private QsstReport mQsstReport = null;
    private JPanel  mConfigPane = null;
    private JPanel  mRightPane = null;
    private JCheckBox mCoverFile = null;
    private JCheckBox mOpenReport = null;
    private JButton mExecute = null;
    private JLabel  mMessageLabel = null;

    private JScrollPane mFilesPane = null;
    private JScrollPane mOperationPane = null;
    private CheckTable mFileTable = null;
    private FileTableModel mFileTableModel = null;
    private String[] mColumnNames = new String[] { "Check", "Name" };
    private Timer mTimer = null;
    private String mLoggingPath = null;

    public ReportPane(QsstReport qsstReport) {
        setOrientation(JSplitPane.HORIZONTAL_SPLIT);
        setResizeWeight(0.5);
        setOneTouchExpandable(true);
        mQsstReport = qsstReport;

        int width = mQsstReport.getAppWidth();
        int minHeight = 200;//mQsstReport.getAppHeight();

        mFileTableModel = new FileTableModel(mColumnNames);
        mFileTable = new CheckTable();
        mFileTable.setModel(mFileTableModel);
        mFileTable.setCheckHeaderColumn(0);
        mFileTable.setEnabled(true);
        mFileTable.setRowHeight(30);
        mFileTable.setBorder(BorderFactory.createEtchedBorder());
        mFileTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        mFileTable.getTableHeader().setReorderingAllowed(false);
        mFileTable.setShowGrid(false);
        mFileTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        mFileTable.setDefaultRenderer(Object.class, new FileTableRenderer());
        mFileTable.setVisible(true);
        mFileTable.setCheckedListener(this);

        mConfigPane = new JPanel(null);
        mConfigPane.setBounds(20, 10, 240, 90);
        mConfigPane.setBorder(BorderFactory.createTitledBorder("Cofniguration"));

        mCoverFile = new JCheckBox("Cover the old report files");
        mCoverFile.setToolTipText("Cover the old report files");
        mCoverFile.setBounds(20, 20, 200, 30);
        mCoverFile.setSelected(true);
        mOpenReport = new JCheckBox("Open the Report after completion");
        mOpenReport.setToolTipText("Open the Report after completion");
        mOpenReport.setBounds(20, 50, 200, 30);
        mOpenReport.setSelected(true);

        mConfigPane.add(mCoverFile);
        mConfigPane.add(mOpenReport);

        //generate button
        mExecute = new JButton("Generate");
        mExecute.setForeground(Color.RED);
        mExecute.setFont(new Font("宋体", Font.BOLD, 15));
        mExecute.setBounds(20, (mConfigPane.getSize().height + 20), 150, 30);
        mExecute.setActionCommand(BUTTON_CMD_EXECUTE);
        mExecute.setToolTipText("Generate the report");
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

        mFilesPane = new JScrollPane(mFileTable,ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
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

        mQsstReport.addWindowListener(new QsstWindowListener());
    }

    public void resizeComponent(int newValue){
        System.out.println("LeftWidth:"+newValue);
        TableColumn column = mFileTable.getColumn(mColumnNames[1]);
        JScrollBar scrollBar = mFilesPane.getVerticalScrollBar();
        int newWidth = newValue-mFileTable.getColumn(mColumnNames[0]).getWidth()-2;
        if(scrollBar.isShowing()) {
            newWidth = newWidth - scrollBar.getWidth();
        }
        column.setPreferredWidth(newWidth);

        int rightWidth = getWidth() - newValue;
        System.out.println("right:"+rightWidth);
//        mConfigPane.setPreferredSize(new Dimension(rightWidth-20, (int)mConfigPane.getPreferredSize().getHeight()));

        mConfigPane.setBounds(20, 10, rightWidth-40, 90);
        Dimension btnDimension = mExecute.getSize();
        mExecute.setBounds((rightWidth-btnDimension.width)/2, (mConfigPane.getSize().height + 20), 150, 30);
        mMessageLabel.setBounds(20, mExecute.getLocation().y+mExecute.getHeight()+5, rightWidth-40, 25);
    }

    public void refresh() {
        refresh(new File(mLoggingPath));
    }

    @Override
    public void refresh(Object object) {
        if(object instanceof File) {
            File loggingDir = (File)object;
            mLoggingPath = loggingDir.getAbsolutePath();
            File[] files = loggingDir.listFiles();
            List<FileBean> fileBeans = new ArrayList<FileBean>();
            List<File> selectFiles = mFileTableModel.getSelectedFiles();
            try {
                for(File file:files) {
                    if(file.isDirectory()) {
                        FileBean fileBean = new FileBean();
                        fileBean.setCheck(isChecked(selectFiles,file.getAbsolutePath()));
                        fileBean.setFile(file);
                        fileBeans.add(fileBean);
                    }
                }
                mFileTableModel.setFileBeans(fileBeans);
                mFileTable.updateUI();
                mFileTable.checkColumnHeader();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    private boolean isChecked(List<File> selectFiles, String filePath) {
        if(selectFiles==null) {
            return false;
        }
        for(File file: selectFiles) {
            if(file.getAbsolutePath().equals(filePath)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void actionPerformed(ActionEvent event) {
        String comm = event.getActionCommand();
        if(BUTTON_CMD_EXECUTE.endsWith(comm)) {
            List<File> selectedFiles = mFileTableModel.getSelectedFiles();
            if(selectedFiles.size() > 0) {
                new GenerateReportThread(selectedFiles).start();
            } else {
                showMessage("Please choose a logging directory firstly");
            }
        }
    }

    @Override
    public void onStatusChanged(int row, boolean isChecked) {

    }

    public void setGenerating(boolean status) {
        mExecute.setEnabled(!status);
        mOpenReport.setEnabled(!status);
        mCoverFile.setEnabled(!status);
        if(status) {
            mExecute.setText("Generating");
        } else{
            mExecute.setText("Generate");
        }
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

    private void openReportFile(String path) {
        mQsstReport.addLogging("Open:"+path);
        File loggingPath = new File(path);
        if(!loggingPath.exists()) {
            showMessage("the report file is not exist");
            return;
        }
      //wether your system support Java AWT Desktop?
        if(Desktop.isDesktopSupported()){
            try {
                //create a uri
                URI uri = new File(path).toURI();
                //get the desktop
                Desktop dp = Desktop.getDesktop();
                //check the system wether support the browse
                if(dp.isSupported(Action.BROWSE)){
                    //open the uri
                    dp.browse(uri);
                }
            } catch(NullPointerException e){
                //if the uri is null
                e.printStackTrace();
            } catch (IOException e) {
                //can not get the default browser
                e.printStackTrace();
            }
        }
        else{
            showMessage("Sorry, Can not support to open the report on your computer.");
        }
//another method to open the link
//      try {
//      Runtime.getRuntime().exec("rundll32 url.dll,FileProtocolHandler http://www.baidu.com");
//  } catch (IOException e) {
//      e.printStackTrace();
//  }
    }

    class GenerateReportThread extends Thread {
        List<File> selectedFiles = null;
        public GenerateReportThread(List<File> selectedFiles) {
            this.selectedFiles =selectedFiles;
        }
        @Override
        public void run() {
            if(selectedFiles==null || selectedFiles.size()==0) {
                return;
            }
            setGenerating(true);
            for(File file: selectedFiles) {
                String loggingPath = ReportFactory.generateReport(file.getAbsolutePath(),null);
                if(!Utils.isEmpty(loggingPath)) {
                    mQsstReport.addLogging("Report:"+loggingPath);
                    if(mOpenReport.isSelected()) {
                        openReportFile(loggingPath);
                    }
                } else {
                    mQsstReport.addLogging("Generate report feailed:"+file.getAbsolutePath());
                }
            }
            setGenerating(false);
        }
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
            }else{

                JLabel label = new JLabel();
                label.setFont(new Font(table.getFont().toString(), Font.BOLD, 14));
                label.setText(value.toString());
                label.setVisible(true);
                label.setOpaque(true);
                return label;
            }
        }

    }

    class QsstWindowListener implements WindowListener {
        @Override
        public void windowOpened(WindowEvent e) {
            File file = new File(Constant.CONFIG_PATH);
            String  loggingPath = null;
            Workspace wrokspace = ConfigFactory.getInstance().getLoggingWorkspace();
            if(file.exists()
                    && (wrokspace = ConfigFactory.getInstance().getLoggingWorkspace()) !=null
                    && !ReportUtils.isEmpty(loggingPath = wrokspace.getLoggingDir())) {
                if(! new File(loggingPath).exists()) {
                    showInitDialog("The old logging workspace is unavailable, please choose another");
                } else{
                    mLoggingPath = loggingPath;
                    refresh();
                }
            } else {
                showInitDialog(null);
            }
        }

        private void showInitDialog(String message) {
            (new InitDialog(mQsstReport, ReportPane.this,message)).setVisible(true);
        }
        @Override
        public void windowClosing(WindowEvent e) {
        }

        @Override
        public void windowClosed(WindowEvent e) {
        }

        @Override
        public void windowIconified(WindowEvent e) {
        }

        @Override
        public void windowDeiconified(WindowEvent e) {
        }

        @Override
        public void windowActivated(WindowEvent e) {
        }

        @Override
        public void windowDeactivated(WindowEvent e) {
        }
    }
}
