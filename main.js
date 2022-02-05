const {app, Browserw, BrowserWindow} = require('electron');
let mainWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({})

    mainWindow.loadURL(`file://${__dirname}/index.html`)
})