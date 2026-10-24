import { PythonEditorApp } from "./PythonEditorApp.js";

const app = new PythonEditorApp();
window.pythonEditor = app;          // pratique pour les tests et le débogage depuis la console du navigateur
app.start();
