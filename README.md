# 🧾 Multilanguage Invoice Parser

A powerful invoice parsing application that leverages Google's Gemini AI to extract and analyze information from invoice images. Built with Streamlit, this tool can process invoices in multiple languages and provide detailed insights based on user queries.

## 🌟 Features

- Upload and process invoice images in various formats (JPG, JPEG, PNG)
- Support for multiple languages
- Real-time AI-powered analysis using Google's Gemini-1.5-flash model
- Interactive web interface built with Streamlit
- Custom query support for specific information extraction
- Visual feedback with image preview
- Environment variable support for secure API key management

## 🛠️ Prerequisites

Before running this application, make sure you have Python installed and the following packages:

```bash
pip install streamlit
pip install Pillow
pip install google-generativeai
pip install python-dotenv
```

## 🔑 API Key Setup

1. Obtain a Google Gemini AI API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in the root directory
3. Add your API key to the `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone <repository-url>
cd multilanguage-invoice-parser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## 💻 Usage

1. Access the application through your web browser (typically `http://localhost:8501`)
2. Enter your query in the "Input Prompt" field
3. Upload an invoice image using the file uploader
4. Click "Tell me about image" to get AI-powered analysis
5. View the response below the image

## 📁 Project Structure

```
multilanguage-invoice-parser/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (API key)
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🔧 Core Functions

### `get_gemini_response(input_text, image_data, prompt)`
- Processes the image and query using Gemini AI
- Returns analyzed text response

### `input_image_details(uploaded_image)`
- Handles image upload and formatting
- Prepares image data for AI processing

## 📋 Requirements

```txt
streamlit==1.27.0
Pillow==10.0.0
google-generativeai==0.3.0
python-dotenv==1.0.0
```

## 🛡️ Environment Variables

The following environment variables are required:

- `GOOGLE_API_KEY`: Your Google Gemini AI API key

## 🔍 Supported Image Formats

- JPG/JPEG
- PNG

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Troubleshooting

Common issues and solutions:

1. **API Key Error**
   - Ensure your `.env` file is properly configured
   - Verify your API key is valid and has necessary permissions

2. **Image Upload Issues**
   - Check if the image format is supported
   - Ensure the image file size is within limits

3. **Response Errors**
   - Verify your internet connection
   - Check if the Gemini AI service is available

## 🙏 Acknowledgments

- Google Gemini AI team for the powerful AI model
- Streamlit team for the excellent web framework
- PIL (Python Imaging Library) for image processing capabilities

## 📈 Future Enhancements

Potential improvements that could be added:

1. Batch processing of multiple invoices
2. Export functionality for parsed data
3. Support for additional file formats
4. Custom templates for specific invoice types
5. Integration with accounting software

## 💡 Usage Tips

1. For best results, ensure images are clear and well-lit
2. Frame your questions specifically for more accurate responses
3. Use high-resolution images when possible
4. Test different query formulations to get optimal results
