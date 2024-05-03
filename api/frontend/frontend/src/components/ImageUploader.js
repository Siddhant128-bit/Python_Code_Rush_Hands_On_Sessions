import React from 'react';
import axios from 'axios';
import './app.css';

class ImageUpload extends React.Component {
  state = {
    selectedFile: null,
    imageUrl: '',
    predictionResult: null,
    error: null
  };
  handleFileChange = (event) => {
    const file = event.target.files[0];
    this.setState({
      selectedFile: file,
      imageUrl: URL.createObjectURL(file)
    });
  };
  handleSubmit = async () => {
    const { selectedFile } = this.state;
    if (selectedFile) {
      const formData = new FormData();
      formData.append('image', selectedFile);
      try {
        const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.setState({ predictionResult: response.data, error: null });
      } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
        this.setState({ error: error.response ? (error.response.data.detail || 'An error occurred while processing the image.') : 'An error occurred while processing the image.' });
      }
    } else {
      console.log('No file selected');
    }
  };
  render() {
    const { imageUrl, predictionResult, error } = this.state;
    return (
      <div>
        <input type="file" onChange={this.handleFileChange} />
        <button className="button" onClick={this.handleSubmit}>Submit</button>
        {imageUrl && (
          <div className="image-container">
            <img src={imageUrl} alt="Uploaded" className="uploaded-image" />
          </div>
        )}
        {predictionResult && (
          <div className='prediction-result'>
            <h2>Prediction Result</h2>
            <p>Class Label: {predictionResult.class_label}</p>
            <p>Class Probability: {predictionResult.class_probability}</p>
          </div>
        )}
        {error && <p>{error}</p>}
      </div>
    );
  }
}
export default ImageUpload;