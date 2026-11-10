import "../utils/csrf.js";            // doit être chargé en premier (jeton CSRF sur les fetch d'écriture)
import { PythonEditorApp } from "./PythonEditorApp.js";

const app = new PythonEditorApp();
window.pythonEditor = app;          // pratique pour les tests et le débogage depuis la console du navigateur
app.start();
