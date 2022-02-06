const {app, BrowserWindow, } = require('electron');
let mainWindow;

app.on('ready', () => {
    // Cria a janela
    mainWindow = new BrowserWindow({width: 800, height: 600, show: false})
    mainWindow.loadURL(`file://${__dirname}/index.html`)

    // Mostra a janela apenas quando estiver carregada
    mainWindow.once('ready-to-show', () => {
        mainWindow.show();
    })
})