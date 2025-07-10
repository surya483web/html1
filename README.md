<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced AI Chatbot</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow: hidden;
        }

        .app-container {
            display: flex;
            height: 100vh;
            position: relative;
        }

        /* Sidebar History */
        .sidebar {
            width: 320px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 255, 255, 0.2);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 100;
        }

        .sidebar.collapsed {
            transform: translateX(-280px);
        }

        .sidebar-header {
            padding: 24px 20px;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .sidebar-title {
            font-size: 18px;
            font-weight: 700;
            color: #1a1a1a;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .toggle-sidebar {
            background: none;
            border: none;
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            color: #666;
        }

        .toggle-sidebar:hover {
            background: rgba(0, 0, 0, 0.1);
            color: #333;
        }

        .history-list {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }

        .history-item {
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .history-item:hover {
            background: rgba(102, 126, 234, 0.1);
            border-color: rgba(102, 126, 234, 0.2);
            transform: translateX(4px);
        }

        .history-item.active {
            background: rgba(102, 126, 234, 0.15);
            border-color: #667eea;
        }

        .history-item-title {
            font-weight: 600;
            color: #1a1a1a;
            font-size: 14px;
            margin-bottom: 4px;
            line-height: 1.4;
        }

        .history-item-preview {
            font-size: 12px;
            color: #666;
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .history-item-time {
            font-size: 11px;
            color: #999;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        /* Main Chat Area */
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .chat-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 20px 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .chat-title {
            font-size: 24px;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .ai-features-toggle {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .ai-features-toggle:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 24px;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(20px);
        }

        .message {
            display: flex;
            gap: 12px;
            margin-bottom: 24px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .message.user {
            flex-direction: row-reverse;
        }

        .message-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: white;
            flex-shrink: 0;
            font-weight: 600;
        }

        .message.user .message-avatar {
            background: linear-gradient(135deg, #667eea, #764ba2);
        }

        .message.bot .message-avatar {
            background: linear-gradient(135deg, #f093fb, #f5576c);
        }

        .message-content {
            flex: 1;
            background: white;
            padding: 16px 20px;
            border-radius: 16px;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
            position: relative;
            line-height: 1.6;
        }

        .message.user .message-content {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .message.bot .message-content {
            background: white;
            color: #333;
        }

        .message-time {
            font-size: 11px;
            opacity: 0.6;
            margin-top: 8px;
        }

        /* Input Area */
        .input-area {
            padding: 24px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.2);
        }

        .input-container {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            gap: 12px;
            align-items: flex-end;
        }

        .input-wrapper {
            flex: 1;
            position: relative;
        }

        .input-field {
            width: 100%;
            padding: 16px 20px;
            border: 2px solid rgba(0, 0, 0, 0.1);
            border-radius: 16px;
            font-size: 16px;
            font-family: inherit;
            background: white;
            transition: all 0.2s ease;
            resize: none;
            max-height: 120px;
            min-height: 52px;
        }

        .input-field:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
        }

        .input-actions {
            display: flex;
            gap: 8px;
        }

        .action-btn {
            width: 52px;
            height: 52px;
            border: none;
            border-radius: 16px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .action-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }

        .action-btn.recording {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            animation: pulse 2s infinite;
        }

        .action-btn.active {
            background: linear-gradient(135deg, #10ac84, #1dd1a1);
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Camera Preview */
        .camera-preview {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 280px;
            height: 210px;
            background: #000;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            z-index: 1000;
            display: none;
        }

        .camera-preview.active {
            display: block;
        }

        .camera-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .camera-controls {
            position: absolute;
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
        }

        .camera-btn {
            width: 40px;
            height: 40px;
            border: none;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .camera-btn:hover {
            background: white;
            transform: scale(1.1);
        }

        /* AI Features Panel */
        .ai-features-panel {
            position: fixed;
            top: 80px;
            right: 20px;
            width: 280px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
            z-index: 1000;
            display: none;
        }

        .ai-features-panel.active {
            display: block;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .features-title {
            font-size: 16px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .feature-btn {
            width: 100%;
            padding: 12px 16px;
            border: none;
            border-radius: 12px;
            background: rgba(102, 126, 234, 0.1);
            color: #333;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
            text-align: left;
        }

        .feature-btn:hover {
            background: rgba(102, 126, 234, 0.2);
            transform: translateX(4px);
        }

        .feature-btn.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        /* Status Indicator */
        .status-indicator {
            position: fixed;
            bottom: 120px;
            right: 20px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 12px;
            padding: 12px 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            z-index: 1000;
            display: none;
        }

        .status-indicator.active {
            display: flex;
            align-items: center;
            gap: 8px;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .status-text {
            font-size: 14px;
            color: #333;
            font-weight: 500;
        }

        .thinking-dots {
            display: flex;
            gap: 2px;
        }

        .thinking-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #667eea;
            animation: thinking 1.4s infinite;
        }

        .thinking-dot:nth-child(2) { animation-delay: 0.2s; }
        .thinking-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes thinking {
            0%, 80%, 100% { transform: scale(1); opacity: 0.5; }
            40% { transform: scale(1.2); opacity: 1; }
        }

        /* Code Blocks */
        .code-block {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 16px;
            margin: 12px 0;
            font-family: 'Fira Code', 'Consolas', monospace;
            font-size: 14px;
            overflow-x: auto;
            position: relative;
        }

        .code-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 8px;
            padding-bottom: 8px;
            border-bottom: 1px solid #e9ecef;
        }

        .code-language {
            font-size: 12px;
            color: #666;
            font-weight: 600;
        }

        .copy-code {
            background: none;
            border: none;
            color: #666;
            cursor: pointer;
            font-size: 12px;
            padding: 4px 8px;
            border-radius: 4px;
            transition: all 0.2s ease;
        }

        .copy-code:hover {
            background: #e9ecef;
            color: #333;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                position: fixed;
                top: 0;
                left: 0;
                height: 100vh;
                z-index: 200;
            }

            .sidebar.collapsed {
                transform: translateX(-100%);
            }

            .main-content {
                width: 100%;
            }

            .camera-preview {
                width: calc(100% - 40px);
                height: 200px;
            }

            .ai-features-panel {
                width: calc(100% - 40px);
            }

            .input-container {
                flex-direction: column;
                gap: 12px;
            }

            .input-actions {
                justify-content: center;
            }
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.05);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #764ba2, #667eea);
        }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Sidebar History -->
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title">
                    <i class="fas fa-history"></i>
                    Chat History
                </div>
                <button class="toggle-sidebar" id="toggleSidebar">
                    <i class="fas fa-chevron-left"></i>
                </button>
            </div>
            <div class="history-list" id="historyList">
                <!-- History items will be populated here -->
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
            <div class="chat-header">
                <div class="chat-title">
                    <i class="fas fa-robot"></i>
                    Advanced AI Assistant
                </div>
                <button class="ai-features-toggle" id="featuresToggle">
                    <i class="fas fa-magic"></i>
                    AI Tools
                </button>
            </div>

            <div class="chat-messages" id="chatMessages">
                <div class="message bot">
                    <div class="message-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="message-content">
                        <p>👋 Hello! I'm your advanced AI assistant with powerful capabilities:</p>
                        <br>
                        <p><strong>🎤 Voice Recognition:</strong> Speak naturally and I'll understand</p>
                        <p><strong>📷 Camera Integration:</strong> Analyze images and visual content</p>
                        <p><strong>💻 Code Generation:</strong> Create, debug, and explain code</p>
                        <p><strong>✨ Creative Writing:</strong> Stories, poems, and creative content</p>
                        <p><strong>📊 Data Analysis:</strong> Process and analyze information</p>
                        <p><strong>🌍 Multi-language:</strong> Translation and communication</p>
                        <p><strong>🧮 Math & Science:</strong> Solve complex problems</p>
                        <br>
                        <p>How can I help you today? Try using voice commands or ask me anything!</p>
                        <div class="message-time">Just now</div>
                    </div>
                </div>
            </div>

            <div class="input-area">
                <div class="input-container">
                    <div class="input-wrapper">
                        <textarea class="input-field" id="messageInput" placeholder="Type your message here..." rows="1"></textarea>
                    </div>
                    <div class="input-actions">
                        <button class="action-btn" id="voiceBtn" title="Voice Input">
                            <i class="fas fa-microphone"></i>
                        </button>
                        <button class="action-btn" id="cameraBtn" title="Camera">
                            <i class="fas fa-camera"></i>
                        </button>
                        <button class="action-btn" id="sendBtn" title="Send Message">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Camera Preview -->
        <div class="camera-preview" id="cameraPreview">
            <video class="camera-video" id="cameraVideo" autoplay muted></video>
            <div class="camera-controls">
                <button class="camera-btn" id="captureBtn" title="Capture Image">
                    <i class="fas fa-camera"></i>
                </button>
                <button class="camera-btn" id="closeCameraBtn" title="Close Camera">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        </div>

        <!-- AI Features Panel -->
        <div class="ai-features-panel" id="aiFeatures">
            <div class="features-title">
                <i class="fas fa-magic"></i>
                AI Tools & Features
            </div>
            <button class="feature-btn" onclick="activateFeature('general')">
                <i class="fas fa-comments"></i>
                General Chat
            </button>
            <button class="feature-btn" onclick="activateFeature('code')">
                <i class="fas fa-code"></i>
                Code Assistant
            </button>
            <button class="feature-btn" onclick="activateFeature('creative')">
                <i class="fas fa-feather-alt"></i>
                Creative Writing
            </button>
            <button class="feature-btn" onclick="activateFeature('analysis')">
                <i class="fas fa-chart-line"></i>
                Data Analysis
            </button>
            <button class="feature-btn" onclick="activateFeature('translate')">
                <i class="fas fa-language"></i>
                Translator
            </button>
            <button class="feature-btn" onclick="activateFeature('math')">
                <i class="fas fa-calculator"></i>
                Math Solver
            </button>
            <button class="feature-btn" onclick="activateFeature('image')">
                <i class="fas fa-image"></i>
                Image Analysis
            </button>
        </div>

        <!-- Status Indicator -->
        <div class="status-indicator" id="statusIndicator">
            <div class="status-text" id="statusText">AI is thinking</div>
            <div class="thinking-dots">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
        </div>
    </div>

    <script>
        // Global variables
        let chatHistory = [];
        let conversationHistory = [];
        let isRecording = false;
        let recognition = null;
        let cameraStream = null;
        let currentFeature = 'general';
        let messageCounter = 0;

        // Initialize application
        document.addEventListener('DOMContentLoaded', function() {
            initializeApp();
        });

        function initializeApp() {
            setupEventListeners();
            initializeSpeechRecognition();
            setupAutoResize();
            loadDefaultHistory();
            console.log('🚀 AI Assistant initialized successfully!');
        }

        function setupEventListeners() {
            // Send message
            document.getElementById('sendBtn').addEventListener('click', sendMessage);
            document.getElementById('messageInput').addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });

            // Voice recognition
            document.getElementById('voiceBtn').addEventListener('click', toggleVoiceRecognition);

            // Camera
            document.getElementById('cameraBtn').addEventListener('click', toggleCamera);
            document.getElementById('captureBtn').addEventListener('click', captureImage);
            document.getElementById('closeCameraBtn').addEventListener('click', closeCamera);

            // Sidebar toggle
            document.getElementById('toggleSidebar').addEventListener('click', toggleSidebar);

            // Features panel
            document.getElementById('featuresToggle').addEventListener('click', toggleFeaturesPanel);

            // Click outside to close panels
            document.addEventListener('click', function(e) {
                const featuresPanel = document.getElementById('aiFeatures');
                const featuresToggle = document.getElementById('featuresToggle');
                
                if (!featuresPanel.contains(e.target) && !featuresToggle.contains(e.target)) {
                    featuresPanel.classList.remove('active');
                }
            });
        }

        function initializeSpeechRecognition() {
            if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = 'en-US';

                recognition.onstart = function() {
                    isRecording = true;
                    document.getElementById('voiceBtn').classList.add('recording');
                    showStatus('🎤 Listening...');
                };

                recognition.onresult = function(event) {
                    const transcript = event.results[0][0].transcript;
                    document.getElementById('messageInput').value = transcript;
                    hideStatus();
                    // Auto-send voice messages
                    setTimeout(() => sendMessage(), 500);
                };

                recognition.onend = function() {
                    isRecording = false;
                    document.getElementById('voiceBtn').classList.remove('recording');
                    hideStatus();
                };

                recognition.onerror = function(event) {
                    console.error('Speech recognition error:', event.error);
                    isRecording = false;
                    document.getElementById('voiceBtn').classList.remove('recording');
                    hideStatus();
                    showStatus('❌ Voice recognition error. Please try again.');
                    setTimeout(hideStatus, 3000);
                };
            } else {
                console.warn('Speech recognition not supported in this browser');
            }
        }

        function setupAutoResize() {
            const textarea = document.getElementById('messageInput');
            textarea.addEventListener('input', function() {
                this.style.height = 'auto';
                this.style.height = Math.min(this.scrollHeight, 120) + 'px';
            });
        }

        function toggleVoiceRecognition() {
            if (!recognition) {
                showStatus('❌ Speech recognition not supported in your browser');
                setTimeout(hideStatus, 3000);
                return;
            }

            if (isRecording) {
                recognition.stop();
            } else {
                recognition.start();
            }
        }

        async function toggleCamera() {
            const cameraPreview = document.getElementById('cameraPreview');
            const cameraBtn = document.getElementById('cameraBtn');

            if (cameraStream) {
                closeCamera();
            } else {
                try {
                    cameraStream = await navigator.mediaDevices.getUserMedia({ 
                        video: { width: 1280, height: 720 } 
                    });
                    document.getElementById('cameraVideo').srcObject = cameraStream;
                    cameraPreview.classList.add('active');
                    cameraBtn.classList.add('active');
                } catch (error) {
                    console.error('Error accessing camera:', error);
                    showStatus('❌ Camera access denied. Please check permissions.');
                    setTimeout(hideStatus, 3000);
                }
            }
        }

        function captureImage() {
            if (!cameraStream) return;

            const video = document.getElementById('cameraVideo');
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0);

            const imageData = canvas.toDataURL('image/jpeg', 0.8);
            
            // Add captured image message
            addMessage('user', '📸 Image captured for analysis');
            
            // Simulate AI image analysis
            setTimeout(() => {
                analyzeImage(imageData);
            }, 1500);
        }

        function analyzeImage(imageData) {
            const analyses = [
                "🔍 **Image Analysis Complete**\n\nI can see this is a real-time image captured from your camera. The image shows:\n\n• Clear visual composition with good lighting\n• Various objects and details in the frame\n• Color palette and contrast levels are well-balanced\n\nI can help you analyze specific aspects of this image or answer questions about what I observe. What would you like to know more about?",
                "📊 **Visual Analysis Results**\n\nBased on the captured image, I can detect:\n\n• **Scene Type:** Indoor/Outdoor environment\n• **Objects:** Multiple elements visible in frame\n• **Quality:** High resolution capture\n• **Lighting:** Natural/Artificial light sources\n\nWould you like me to focus on any particular aspect of the image?",
                "🎯 **Image Processing Complete**\n\nI've successfully analyzed your captured image. Here's what I found:\n\n• **Technical Quality:** Good exposure and focus\n• **Content Analysis:** Various visual elements detected\n• **Composition:** Well-framed capture\n\nI can provide more detailed analysis of specific elements if you'd like. What aspects are you most interested in?",
                "🔎 **Smart Image Recognition**\n\nYour image has been processed using advanced AI vision capabilities:\n\n• **Visual Elements:** Successfully identified multiple components\n• **Scene Understanding:** Context and environment analyzed\n• **Detail Recognition:** Fine details and textures processed\n\nI'm ready to answer any specific questions about what I see in your image!"
            ];
            
            const randomAnalysis = analyses[Math.floor(Math.random() * analyses.length)];
            addMessage('bot', randomAnalysis);
        }

        function closeCamera() {
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStream = null;
                document.getElementById('cameraPreview').classList.remove('active');
                document.getElementById('cameraBtn').classList.remove('active');
            }
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
