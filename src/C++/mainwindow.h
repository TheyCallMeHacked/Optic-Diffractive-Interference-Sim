#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QWidget
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void onWavelengthChange(int f);
    void onSlitWidthChange(int f);
    void onSlitSeparationChange(int f);

private:
    void makeConnection();
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H