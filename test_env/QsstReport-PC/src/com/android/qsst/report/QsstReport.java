package com.android.qsst.report;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.FontMetrics;
import java.awt.Rectangle;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JSplitPane;
import javax.swing.JTabbedPane;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.plaf.TabbedPaneUI;
import javax.swing.plaf.basic.BasicTabbedPaneUI;

import com.android.qsst.report.util.QsstResourse;
import com.android.qsst.report.util.ReportUtils;

public class QsstReport extends JFrame {

    private static final long serialVersionUID = 1L;
    private     static final String TAB_REPORT   = "Report";
    private     static final String TAB_EXPORT   = "Log";

    private int mAppWidth = 700;
    private int mAppHeight = 500;
    private QsstReportMenuBar       mMenuBar            = null;
    private JTabbedPane             mTabPane          = null;
    private JSplitPane             mMainPane          = null;
    private DevicePane              mDevicePane = null;
    private ReportPane              mReportPane = null;
    private LoggingPanel            mLoggingPanel = null;
    /**
     * Launch the application
     * @param args
     */
    public static void main(String args[]) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    QsstReport frame = new QsstReport();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public QsstReport() {
        //the the default ui
        ReportUtils.setLookAndFeel();

        getContentPane().setLayout(new BorderLayout());
        //set the app frame is in the center of the screen
        int screenWith = Toolkit.getDefaultToolkit().getScreenSize().width;
        int screenheight = Toolkit.getDefaultToolkit().getScreenSize().height;
        setBounds((screenWith-mAppWidth)/2, (screenheight - mAppHeight)/2, mAppWidth, mAppHeight);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        setTitle(Constant.APP_NAME+" - "+Constant.APP_VERSION);
        setIconImage(this.getToolkit().createImage(QsstResourse.url_icon));

        mMenuBar = new QsstReportMenuBar(this);
        setJMenuBar(mMenuBar);

        initMainFrame();
    }

    public void initMainFrame()
    {
        mTabPane = new JTabbedPane();
        mTabPane.setTabLayoutPolicy(JTabbedPane.SCROLL_TAB_LAYOUT);
        mTabPane.setUI(new BasicTabbedPaneUI() {

            @Override
            protected int calculateTabWidth(int tabPlacement, int tabIndex,
                    FontMetrics metrics) {
                return super.calculateTabWidth(tabPlacement, tabIndex, metrics) + 50;
            }
        });

        mReportPane =new ReportPane(this);
        mDevicePane = new DevicePane(this);

        mTabPane.addTab(TAB_REPORT, mReportPane);
        mTabPane.addTab(TAB_EXPORT, mDevicePane);
        mTabPane.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                int selectIndex = mTabPane.getSelectedIndex();
                switch (selectIndex) {
                case 0:
                    mReportPane.refresh();
                    break;
                case 1:
                    mDevicePane.refreshTable();
                    break;
                }
            }
        });

        mLoggingPanel = new LoggingPanel(this);
        mLoggingPanel.setMinimumSize(new Dimension(mAppWidth, 100));

        mMainPane = new JSplitPane();
        mMainPane.setOrientation(JSplitPane.VERTICAL_SPLIT);
        mMainPane.setResizeWeight(0.7);
        mMainPane.setOneTouchExpandable(true);

        mMainPane.setTopComponent(mTabPane);
        mMainPane.setBottomComponent(mLoggingPanel);
        add(mMainPane,BorderLayout.CENTER);
    }
    public int getAppHeight() {
        return mAppHeight;
    }
    public int getAppWidth() {
        return mAppWidth;
    }
    public void addLogging(String msg) {
        mLoggingPanel.addLog(msg);
    }
}
