
import React from 'react';
import './App.css';
import ImageUploader from './components/ImageUploader'; // Corrected import path

function App() {
  return (
    <div className="App">
      <h1>Image Classifier</h1>
      <ImageUploader />
    </div>
  );
}

export default App;
