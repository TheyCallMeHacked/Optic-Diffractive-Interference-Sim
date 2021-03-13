#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QSlider>
#include "diffraction.h"

#include <stdio.h>

Wave wave(350,350,380,0,0);

MainWindow::MainWindow(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    makeConnection();

    wave.draw(ui->waveViewer, ui->fringeViewer);
}

MainWindow::~MainWindow() {
    delete ui;
}


void MainWindow::onWavelengthChange(int f) {
    ui->wavelengthLabel->setText(QString("Longueur d'onde: ").append(QString::number(f)).append("nm"));
    ui->wavelengthLabel->adjustSize();
    wave.wl = f;
    wave.draw(ui->waveViewer, ui->fringeViewer);
}

void MainWindow::onSlitWidthChange(int f) {
    ui->slitWidthLabel->setText(QString("Largeur des fentes: ").append(QString::number(((float)f)/1000)).append("µm"));
    ui->slitWidthLabel->adjustSize();
    wave.swidth = f;
    wave.draw(ui->waveViewer, ui->fringeViewer);
}

void MainWindow::onSlitSeparationChange(int f){
    ui->slitSeparationLabel->setText(QString("Espacement des fentes: ").append(QString::number(((float)f)/100)).append("µm"));
    ui->slitSeparationLabel->adjustSize();
    wave.ssep = ((float)f)/100;
    wave.draw(ui->waveViewer, ui->fringeViewer);
}

void MainWindow::makeConnection() {
    connect(ui->wavelengthSlider, &QSlider::valueChanged, this, &MainWindow::onWavelengthChange);
    connect(ui->slitWidthSlider, &QSlider::valueChanged, this, &MainWindow::onSlitWidthChange);
    connect(ui->slitSeparationSlider, &QSlider::valueChanged, this, &MainWindow::onSlitSeparationChange);
    ui->wavelengthSlider->setValue(380);
}
