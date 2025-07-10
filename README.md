 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced AI Assistant</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            overflow: hidden;
        }

        .container {
            display: flex;
            height: 100vh;
            position: relative;
        }

        /* History Dashboard */
        .history-panel {
            width: 300px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 0 20px 20px 0;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .history-panel.collapsed {
            transform: translateX(-250px);
        }

        .history-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e0e0e0;
        }

        .history-title {
            font-size: 18px;
            font-weight: 600;
            color: #333;
        }

        .toggle-btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            color: white;
            cursor: pointer;
            font-size: 16px;
            transition: transform 0.2s ease;
        }

        .toggle-btn:hover {
            transform: scale(1.1);
        }

        .history-list {
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .history-item {
            padding: 12px;
            background: rgba(102, 126, 234, 0.1);
            border-radius: 10px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            border-left: 4px solid transparent;
        }

        .history-item:hover {
            background: rgba(102, 126, 234, 0.2);
            border-left-color: #667eea;
            transform: translateX(5px);
        }

        .history-item-title {
            font-weight: 500;
            color: #333;
            margin-bottom: 5px;
        }

        .history-item-time {
            font-size: 12px;
            color: #666;
        }

        /* Main Chat Area */
        .main-chat {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .chat-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 20px 20px 0 0;
            margin: 20px 20px 0 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .chat-title {
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            margin: 0 20px;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border-radius: 0;
        }

        .message {
            margin-bottom: 20px;
            display: flex;
            align-items: flex-start;
            gap: 12px;
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
            font-weight: bold;
            color: white;
            flex-shrink: 0;
        }

        .message.user .message-avatar {
            background: linear-gradient(45deg, #667eea, #764ba2);
        }

        .message.bot .message-avatar {
            background: linear-gradient(45deg, #f093fb, #f5576c);
        }

        .message-content {
            background: white;
            padding: 15px 20px;
            border-radius: 20px;
            max-width: 70%;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        .message.user .message-content {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
        }

        .message.bot .message-content {
            background: linear-gradient(45deg, #f8f9fa, #e9ecef);
            color: #333;
        }

        /* Input Area */
        .input-area {
            padding: 20px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 0 0 20px 20px;
            margin: 0 20px 20px 20px;
            box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1);
        }

        .input-container {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .input-field {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid transparent;
            border-radius: 25px;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.9);
            transition: all 0.3s ease;
        }

        .input-field:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.2);
        }

        .action-btn {
            width: 50px;
            height: 50px;
            border: none;
            border-radius: 50%;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .action-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .action-btn.recording {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            animation: pulse 1s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Camera Preview */
        .camera-preview {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 200px;
            height: 150px;
            background: #000;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            z-index: 100;
            display: none;
        }

        .camera-preview video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .camera-controls {
            position: absolute;
            bottom: 5px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
        }

        .camera-btn {
            width: 30px;
            height: 30px;
            border: none;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            font-size: 12px;
            cursor: pointer;
        }

        /* AI Features Panel */
        .ai-features {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            z-index: 50;
        }

        .feature-btn {
            display: block;
            width: 100%;
            padding: 10px 15px;
            margin-bottom: 10px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .feature-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .feature-btn:last-child {
            margin-bottom: 0;
        }

        /* Status Indicator */
        .status-indicator {
            position: absolute;
            bottom: 100px;
            right: 20px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 10px 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            display: none;
        }

        .status-text {
            font-size: 14px;
            color: #333;
            margin: 0;
        }

        .thinking-animation {
            display: inline-block;
            animation: thinking 1.5s infinite;
        }

        @keyframes thinking {
            0%, 60%, 100% { transform: scale(1); }
            30% { transform: scale(1.2); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .history-panel {
                width: 250px;
            }
            
            .history-panel.collapsed {
                transform: translateX(-200px);
            }
            
            .message-content {
                max-width: 85%;
            }
            
            .ai-features {
                position: relative;
                right: auto;
                top: auto;
                margin-bottom: 20px;
            }
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #764ba2, #667eea);
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- History Dashboard -->
        <div class="history-panel" id="historyPanel">
            <div class="history-header">
                <h2 class="history-title">Chat History</h2>
                <button class="toggle-btn" id="toggleHistory">←</button>
            </div>
            <div class="history-list" id="historyList">
                <!-- History items will be populated here -->
            </div>
        </div>

        <!-- Main Chat Area -->
        <div class="main-chat">
            <div class="chat-header">
                <h1 class="chat-title">🤖 Advanced AI Assistant</h1>
            </div>

            <div class="chat-messages" id="chatMessages">
                <div class="message bot">
                    <div class="message-avatar">🤖</div>
                    <div class="message-content">
                        <p>Hello! I'm your advanced AI assistant with voice recognition, camera access, and comprehensive knowledge. I can help you with:</p>
                        <ul style="margin-top: 10px; padding-left: 20px;">
                            <li>Text conversations and Q&A</li>
                            <li>Voice commands and speech recognition</li>
                            <li>Image analysis and camera integration</li>
                            <li>Code generation and debugging</li>
                            <li>Creative writing and brainstorming</li>
                            <li>Data analysis and calculations</li>
                        </ul>
                        <p style="margin-top: 10px;">How can I assist you today?</p>
                    </div>
                </div>
            </div>

            <div class="input-area">
                <div class="input-container">
                    <input type="text" class="input-field" id="messageInput" placeholder="Type your message or use voice/camera...">
                    <button class="action-btn" id="voiceBtn" title="Voice Input">🎤</button>
                    <button class="action-btn" id="cameraBtn" title="Camera">📷</button>
                    <button class="action-btn" id="sendBtn" title="Send Message">📤</button>
                </div>
            </div>

            <!-- Camera Preview -->
            <div class="camera-preview" id="cameraPreview">
                <video id="cameraVideo" autoplay muted></video>
                <div class="camera-controls">
                    <button class="camera-btn" id="captureBtn">📸</button>
                    <button class="camera-btn" id="closeCameraBtn">✕</button>
                </div>
            </div>

            <!-- AI Features Panel -->
            <div class="ai-features">
                <button class="feature-btn" onclick="activateFeature('code')">💻 Code Assistant</button>
                <button class="feature-btn" onclick="activateFeature('creative')">✨ Creative Writing</button>
                <button class="feature-btn" onclick="activateFeature('analysis')">📊 Data Analysis</button>
                <button class="feature-btn" onclick="activateFeature('translate')">🌍 Translator</button>
                <button class="feature-btn" onclick="activateFeature('math')">🧮 Math Solver</button>
            </div>

            <!-- Status Indicator -->
            <div class="status-indicator" id="statusIndicator">
                <p class="status-text" id="statusText">AI is thinking...</p>
            </div>
        </div>
    </div>

    <script>
        // Global variables
        let chatHistory = [];
        let isRecording = false;
        let recognition = null;
        let cameraStream = null;
        let currentFeature = 'general';

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            initializeApp();
        });

        function initializeApp() {
            setupEventListeners();
            initializeSpeechRecognition();
            loadChatHistory();
            setupKeyboardShortcuts();
        }

        function setupEventListeners() {
            // Send message
            document.getElementById('sendBtn').addEventListener('click', sendMessage);
            document.getElementById('messageInput').addEventListener('keypress', function(e) {
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

            // History panel
            document.getElementById('toggleHistory').addEventListener('click', toggleHistoryPanel);
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
                    showStatus('Listening...');
                };

                recognition.onresult = function(event) {
                    const transcript = event.results[0][0].transcript;
                    document.getElementById('messageInput').value = transcript;
                    hideStatus();
                };

                recognition.onend = function() {
                    isRecording = false;
                    document.getElementById('voiceBtn').classList.remove('recording');
                    hideStatus();
                };

                recognition.onerror = function(event) {
                    console.error('Speech recognition error:', event.error);
                    hideStatus();
                    showStatus('Voice recognition error. Please try again.');
                    setTimeout(hideStatus, 3000);
                };
            } else {
                console.log('Speech recognition not supported');
            }
        }

        function toggleVoiceRecognition() {
            if (!recognition) {
                alert('Speech recognition is not supported in your browser');
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
            const video = document.getElementById('cameraVideo');

            if (cameraStream) {
                closeCamera();
            } else {
                try {
                    cameraStream = await navigator.mediaDevices.getUserMedia({ 
                        video: { width: 640, height: 480 } 
                    });
                    video.srcObject = cameraStream;
                    cameraPreview.style.display = 'block';
                } catch (error) {
                    console.error('Error accessing camera:', error);
                    alert('Unable to access camera. Please check permissions.');
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

            const imageData = canvas.toDataURL('image/png');
            
            // Add captured image to chat
            addMessage('user', 'Image captured 📸');
            
            // Simulate AI image analysis
            setTimeout(() => {
                analyzeImage(imageData);
            }, 1000);
        }

        function analyzeImage(imageData) {
            // Simulate AI image analysis
            const analyses = [
                "I can see this is an image. Based on the visual elements, this appears to be a photo taken with your camera.",
                "This image shows various objects and lighting conditions. The composition suggests it was taken in real-time.",
                "I've analyzed the image structure and can help you with questions about what I observe in the photo.",
                "The image has been successfully captured and processed. I can discuss the visual elements I detect."
            ];
            
            const randomAnalysis = analyses[Math.floor(Math.random() * analyses.length)];
            addMessage('bot', randomAnalysis);
        }

        function closeCamera() {
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStream = null;
                document.getElementById('cameraPreview').style.display = 'none';
            }
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;

            // Add user message
            addMessage('user', message);
            input.value = '';

            // Show thinking status
            showStatus('AI is thinking...');

            // Simulate AI response
            setTimeout(() => {
                const response = generateAIResponse(message);
                addMessage('bot', response);
                hideStatus();
            }, 1000 + Math.random() * 2000);
        }

        function generateAIResponse(message) {
            const responses = {
                code: [
                    "I'd be happy to help you with coding! Here's a solution:\n\n```javascript\nfunction example() {\n    console.log('Hello, World!');\n}\n```\n\nWould you like me to explain how this works?",
                    "Let me analyze your code request and provide a comprehensive solution with best practices.",
                    "I can help you debug, optimize, or create new code. What specific programming challenge are you facing?"
                ],
                creative: [
                    "Here's a creative piece inspired by your request:\n\n*In the realm of imagination, where words dance like fireflies in the twilight...*\n\nWould you like me to continue this story?",
                    "I love creative challenges! Let me craft something unique for you based on your idea.",
                    "Creative writing is one of my favorite tasks. Here's an original piece inspired by your prompt..."
                ],
                analysis: [
                    "Based on the data patterns I can analyze, here are the key insights:\n\n• Trend Analysis: [Simulated results]\n• Statistical Significance: High\n• Recommendations: [Generated suggestions]\n\nWould you like me to dive deeper into any specific aspect?",
                    "I can process and analyze various types of data. What specific metrics or patterns would you like me to examine?",
                    "Data analysis complete! Here are the key findings and actionable insights from your dataset."
                ],
                translate: [
                    "Here's the translation:\n\n**English:** Hello, how are you?\n**Spanish:** Hola, ¿cómo estás?\n**French:** Bonjour, comment allez-vous?\n**German:** Hallo, wie geht es dir?\n\nWould you like translations in other languages?",
                    "I can translate between over 100 languages. What would you like me to translate?",
                    "Translation completed! I've provided accurate translations with cultural context where relevant."
                ],
                math: [
                    "Let me solve this mathematical problem step by step:\n\n**Step 1:** Identify the equation type\n**Step 2:** Apply appropriate mathematical principles\n**Step 3:** Calculate the result\n\n**Answer:** [Calculated result]\n\nWould you like me to show alternative solving methods?",
                    "Mathematics is my specialty! Here's the solution with detailed explanations.",
                    "I've solved your math problem using advanced computational methods. The answer is verified and accurate."
                ],
                general: [
                    "That's a great question! Based on my knowledge, here's what I can tell you: " + message.toLowerCase().includes('what') ? "This is a comprehensive topic that involves multiple aspects." : "I understand your inquiry and here's my detailed response.",
                    "I'd be happy to help you with that! Here's a comprehensive answer based on the latest information available.",
                    "That's an interesting topic! Let me provide you with a detailed and accurate response.",
                    "I can definitely assist you with that question. Here's what I know about this subject.",
                    "Great question! Based on my training data, here's a thorough explanation of this topic."
                ]
            };

            const categoryResponses = responses[currentFeature] || responses.general;
            const randomResponse = categoryResponses[Math.floor(Math.random() * categoryResponses.length)];
            
            return randomResponse;
        }

        function addMessage(sender, content) {
            const messagesContainer = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;
            
            const avatar = document.createElement('div');
            avatar.className = 'message-avatar';
            avatar.textContent = sender === 'user' ? '👤' : '🤖';
            
            const messageContent = document.createElement('div');
            messageContent.className = 'message-content';
            messageContent.innerHTML = formatMessage(content);
            
            messageDiv.appendChild(avatar);
            messageDiv.appendChild(messageContent);
            messagesContainer.appendChild(messageDiv);
            
            // Scroll to bottom
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
            
            // Save to history
            const historyItem = {
                id: Date.now(),
                sender: sender,
                content: content,
                timestamp: new Date().toISOString(),
                title: content.length > 50 ? content.substring(0, 50) + '...' : content
            };
            
            chatHistory.push(historyItem);
            updateHistoryPanel();
            saveChatHistory();
        }

        function formatMessage(content) {
            // Format code blocks
            content = content.replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre style="background: #f8f9fa; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 10px 0;"><code>$2</code></pre>');
            
            // Format inline code
            content = content.replace(/`([^`]+)`/g, '<code style="background: #f8f9fa; padding: 2px 6px; border-radius: 4px; font-family: monospace;">$1</code>');
            
            // Format bold text
            content = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            
            // Format italic text
            content = content.replace(/\*(.*?)\*/g, '<em>$1</em>');
            
            // Format line breaks
            content = content.replace(/\n/g, '<br>');
            
            return content;
        }

        function activateFeature(feature) {
            currentFeature = feature;
            const featureNames = {
                code: 'Code Assistant',
                creative: 'Creative Writing',
                analysis: 'Data Analysis',
                translate: 'Translator',
                math: 'Math Solver'
            };
            
            addMessage('bot', `${featureNames[feature]} mode activated! I'm now optimized for ${feature} tasks. How can I help you?`);
        }

        function toggleHistoryPanel() {
            const historyPanel = document.getElementById('historyPanel');
            const toggleBtn = document.getElementById('toggleHistory');
            
            historyPanel.classList.toggle('collapsed');
            toggleBtn.textContent = historyPanel.classList.contains('collapsed') ? '→' : '←';
        }

        function updateHistoryPanel() {
            const historyList = document.getElementById('historyList');
            historyList.innerHTML = '';
            
            // Group messages by conversation sessions
            const sessions = groupMessagesBySession();
            
            sessions.forEach(session => {
                const sessionDiv = document.createElement('div');
                sessionDiv.className = 'history-item';
                sessionDiv.onclick = () => loadSession(session);
                
                sessionDiv.innerHTML = `
                    <div class="history-item-title">${session.title}</div>
                    <div class="history-item-time">${formatTime(session.timestamp)}</div>
                `;
                
                historyList.appendChild(sessionDiv);
            });
        }

        function groupMessagesBySession() {
            const sessions = [];
            let currentSession = null;
            
            chatHistory.forEach(message => {
                if (message.sender === 'user') {
                    if (currentSession) {
                        sessions.push(currentSession);
                    }
                    currentSession = {
                        id: message.id,
                        title: message.title,
                        timestamp: message.timestamp,
                        messages: [message]
                    };
                } else if (currentSession) {
                    currentSession.messages.push(message);
                }
            });
            
            if (currentSession) {
                sessions.push(currentSession);
            }
            
            return sessions.reverse();
        }

        function loadSession(session) {
            // This would typically load the full conversation
            // For now, we'll just scroll to show the session was selected
            const messagesContainer = document.getElementById('chatMessages');
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function formatTime(timestamp) {
            const date = new Date(timestamp);
            const now = new Date();
            const diff = now - date;
            
            if (diff < 60000) return 'Just now';
            if (diff < 3600000) return `${Math.floor(diff / 60000)}m ago`;
            if (diff < 86400000) return `${Math.floor(diff / 3600000)}h ago`;
            return date.toLocaleDateString();
        }

        function showStatus(message) {
            const statusIndicator = document.getElementById('statusIndicator');
            const statusText = document.getElementById('statusText');
            
            statusText.innerHTML = message + ' <span class="thinking-animation">●</span>';
            statusIndicator.style.display = 'block';
        }

        function hideStatus() {
            document.getElementById('statusIndicator').style.display = 'none';
        }

        function saveChatHistory() {
            // In a real application, this would save to a database
            // For now, we'll use in-memory storage
            console.log('Chat history saved:', chatHistory.length, 'messages');
        }

        function loadChatHistory() {
            // In a real application, this would load from a database
            // For now, we'll start with an empty history
            chatHistory = [];
        }

        function setupKeyboardShortcuts() {
            document.addEventListener('keydown', function(e) {
                // Ctrl/Cmd + Enter to send message
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                    sendMessage();
                }
                
                // Ctrl/Cmd + / to toggle voice
                if ((e.ctrlKey || e.metaKey) && e.key === '/') {
                    e.preventDefault();
                    toggleVoiceRecognition();
                }
                
                // Ctrl/Cmd + Shift + C to toggle camera
                if ((e.ctrlKey || e.meta
