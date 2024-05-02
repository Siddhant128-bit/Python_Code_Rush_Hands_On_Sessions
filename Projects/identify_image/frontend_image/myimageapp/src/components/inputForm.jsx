// ImageForm.jsx
import React, { useState } from 'react';
import axios from 'axios';
import './inputForm.css'; // Import your CSS file

const ImageForm = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [imagePreview, setImagePreview] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);

    // Display image preview
    const reader = new FileReader();
    reader.onload = () => {
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(selectedFile);
  };

  const handleSubmit = async () => {
    setLoading(true);
    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload/", formData);
      setResult(response.data);
      console.log('Response data:', response.data); 
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
        <h1> Identify The Image</h1>
      <div className="section">
        <h2>Upload Image:</h2>
        <input type="file" onChange={handleFileChange} />
        <div className="section">
        <h2>Image Preview:</h2>
        {imagePreview && (
          <img src={imagePreview} alt="Uploaded" />
        )}
      </div>
        <button className="upload-btn" onClick={handleSubmit} disabled={!file || loading}>
          {loading ? 'Loading...' : 'Submit'}
        </button>
      </div>
     
      <div className="section">
        <h2>Result:</h2>
        {result && result.class_label && ( 
          <p>{result.class_label}</p>
        )}
      </div>
    </div>
  );
};

export default ImageForm;
