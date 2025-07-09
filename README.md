 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Web App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Page transitions */
        .page {
            display: none;
            min-height: 100vh;
            transition: all 0.3s ease;
        }

        .page.active {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Login Page */
        .login-page {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .login-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .login-header h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .login-header p {
            color: #666;
            font-size: 1.1em;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }

        .form-group input {
            width: 100%;
            padding: 15px;
            border: 2px solid #e1e1e1;
            border-radius: 12px;
            font-size: 16px;
            transition: all 0.3s ease;
            background: #f8f9fa;
        }

        .form-group input:focus {
            outline: none;
            border-color: #667eea;
            background: white;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }

        .btn:active {
            transform: translateY(0);
        }

        /* Verification Page */
        .verification-page {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .verification-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 500px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .verification-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            color: white;
        }

        .code-input {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin: 30px 0;
        }

        .code-input input {
            width: 60px;
            height: 60px;
            border: 2px solid #e1e1e1;
            border-radius: 12px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            background: #f8f9fa;
        }

        .code-input input:focus {
            outline: none;
            border-color: #667eea;
            background: white;
        }

        /* Main App Layout */
        .app-layout {
            display: flex;
            min-height: 100vh;
        }

        .sidebar {
            width: 280px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.2);
            padding: 30px 20px;
            box-shadow: 5px 0 20px rgba(0, 0, 0, 0.1);
        }

        .sidebar-header {
            text-align: center;
            margin-bottom: 40px;
        }

        .sidebar-header h2 {
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.8em;
        }

        .nav-menu {
            list-style: none;
        }

        .nav-item {
            margin-bottom: 10px;
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 15px 20px;
            text-decoration: none;
            color: #555;
            border-radius: 12px;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .nav-link:hover, .nav-link.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            transform: translateX(5px);
        }

        .nav-link i {
            margin-right: 12px;
            font-size: 18px;
        }

        .main-content {
            flex: 1;
            padding: 30px;
            background: rgba(255, 255, 255, 0.1);
        }

        .content-header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .content-header h1 {
            color: #333;
            font-size: 2.2em;
            margin-bottom: 10px;
        }

        .content-header p {
            color: #666;
            font-size: 1.1em;
        }

        .content-body {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        /* Dashboard Specific */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 15px;
            padding: 25px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
        }

        .stat-card h3 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .stat-card p {
            font-size: 1.1em;
            opacity: 0.9;
        }

        .activity-feed {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
        }

        .activity-item {
            display: flex;
            align-items: center;
            padding: 15px;
            border-bottom: 1px solid #e1e1e1;
        }

        .activity-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            margin-right: 15px;
        }

        /* Profile Page */
        .profile-card {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
        }

        .profile-avatar {
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            margin-right: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            color: white;
        }

        .profile-info h2 {
            color: #333;
            margin-bottom: 10px;
        }

        .profile-info p {
            color: #666;
            margin-bottom: 5px;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }

        /* Settings Page */
        .settings-section {
            margin-bottom: 30px;
        }

        .settings-section h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .setting-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 12px;
            margin-bottom: 10px;
        }

        .toggle-switch {
            width: 50px;
            height: 25px;
            background: #ddd;
            border-radius: 25px;
            position: relative;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .toggle-switch.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
        }

        .toggle-switch::before {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            width: 21px;
            height: 21px;
            background: white;
            border-radius: 50%;
            transition: transform 0.3s ease;
        }

        .toggle-switch.active::before {
            transform: translateX(25px);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                position: fixed;
                top: 0;
                left: -100%;
                z-index: 1000;
                transition: left 0.3s ease;
                height: 100vh;
                overflow-y: auto;
            }

            .sidebar.mobile-open {
                left: 0;
            }

            .main-content {
                padding: 20px;
            }

            .mobile-menu-btn {
                display: block;
                position: fixed;
                top: 20px;
                left: 20px;
                z-index: 1001;
                background: rgba(255, 255, 255, 0.95);
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                cursor: pointer;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            }

            .form-row {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (min-width: 769px) {
            .mobile-menu-btn {
                display: none;
            }
        }

        /* Animations */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        .pulse {
            animation: pulse 2s infinite;
        }
    </style>
</head>
<body>
    <!-- Login Page -->
    <div id="login-page" class="page active">
        <div class="login-page">
            <div class="login-card">
                <div class="login-header">
                    <h1>Welcome Back</h1>
                    <p>Sign in to your account</p>
                </div>
                <form id="login-form">
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <button type="submit" class="btn">Sign In</button>
                </form>
                <div style="text-align: center; margin-top: 20px;">
                    <p style="color: #666;">Don't have an account? 
                        <a href="#" onclick="showSignUp()" style="color: #667eea; text-decoration: none; font-weight: 600;">Sign Up</a>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- Sign Up Page -->
    <div id="signup-page" class="page">
        <div class="login-page">
            <div class="login-card">
                <div class="login-header">
                    <h1>Create Account</h1>
                    <p>Join us today and get started</p>
                </div>
                <form id="signup-form">
                    <div class="form-group">
                        <label for="signup-name">Full Name</label>
                        <input type="text" id="signup-name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="signup-email">Email Address</label>
                        <input type="email" id="signup-email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="signup-password">Password</label>
                        <input type="password" id="signup-password" name="password" required>
                    </div>
                    <div class="form-group">
                        <label for="signup-confirm-password">Confirm Password</label>
                        <input type="password" id="signup-confirm-password" name="confirm-password" required>
                    </div>
                    <button type="submit" class="btn">Create Account</button>
                </form>
                <div style="text-align: center; margin-top: 20px;">
                    <p style="color: #666;">Already have an account? 
                        <a href="#" onclick="showLogin()" style="color: #667eea; text-decoration: none; font-weight: 600;">Sign In</a>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- Verification Page -->
    <div id="verification-page" class="page">
        <div class="verification-page">
            <div class="verification-card">
                <div class="verification-icon">✉</div>
                <h2>Verify Your Account</h2>
                <p>We've sent a verification code to your email address. Please enter the code below.</p>
                <div class="code-input">
                    <input type="text" maxlength="1" class="code-digit">
                    <input type="text" maxlength="1" class="code-digit">
                    <input type="text" maxlength="1" class="code-digit">
                    <input type="text" maxlength="1" class="code-digit">
                    <input type="text" maxlength="1" class="code-digit">
                    <input type="text" maxlength="1" class="code-digit">
                </div>
                <button class="btn" onclick="verifyCode()">Verify Code</button>
            </div>
        </div>
    </div>

    <!-- Main App -->
    <div id="main-app" class="page">
        <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
        <div class="app-layout">
            <aside class="sidebar" id="sidebar">
                <div class="sidebar-header">
                    <h2>Dashboard</h2>
                </div>
                <nav>
                    <ul class="nav-menu">
                        <li class="nav-item">
                            <a href="#" class="nav-link active" onclick="showPage('dashboard')">
                                <i>📊</i> Dashboard
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('profile')">
                                <i>👤</i> Profile
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('analytics')">
                                <i>📈</i> Analytics
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('messages')">
                                <i>💬</i> Messages
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('projects')">
                                <i>📁</i> Projects
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('team')">
                                <i>👥</i> Team
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="showPage('settings')">
                                <i>⚙️</i> Settings
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="#" class="nav-link" onclick="logout()">
                                <i>🚪</i> Logout
                            </a>
                        </li>
                    </ul>
                </nav>
            </aside>
            <main class="main-content">
                <!-- Dashboard Content -->
                <div id="dashboard-content" class="content-section active">
                    <div class="content-header">
                        <h1>Dashboard</h1>
                        <p>Welcome back! Here's what's happening with your account.</p>
                    </div>
                    <div class="content-body">
                        <div class="stats-grid">
                            <div class="stat-card">
                                <h3>1,234</h3>
                                <p>Total Users</p>
                            </div>
                            <div class="stat-card">
                                <h3>567</h3>
                                <p>Active Projects</p>
                            </div>
                            <div class="stat-card">
                                <h3>89%</h3>
                                <p>Success Rate</p>
                            </div>
                            <div class="stat-card">
                                <h3>$12,345</h3>
                                <p>Revenue</p>
                            </div>
                        </div>
                        <div class="activity-feed">
                            <h3>Recent Activity</h3>
                            <div class="activity-item">
                                <div class="activity-icon">👤</div>
                                <div>
                                    <strong>New user registered</strong>
                                    <p>John Doe joined your team</p>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">📊</div>
                                <div>
                                    <strong>Report generated</strong>
                                    <p>Monthly analytics report is ready</p>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">🚀</div>
                                <div>
                                    <strong>Project launched</strong>
                                    <p>Website redesign project went live</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Profile Content -->
                <div id="profile-content" class="content-section">
                    <div class="content-header">
                        <h1>Profile</h1>
                        <p>Manage your personal information and preferences.</p>
                    </div>
                    <div class="content-body">
                        <div class="profile-card">
                            <div class="profile-avatar">JD</div>
                            <div class="profile-info">
                                <h2>John Doe</h2>
                                <p>john.doe@example.com</p>
                                <p>Senior Developer</p>
                                <p>San Francisco, CA</p>
                            </div>
                        </div>
                        <form>
                            <div class="form-row">
                                <div class="form-group">
                                    <label>First Name</label>
                                    <input type="text" value="John">
                                </div>
                                <div class="form-group">
                                    <label>Last Name</label>
                                    <input type="text" value="Doe">
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label>Email</label>
                                    <input type="email" value="john.doe@example.com">
                                </div>
                                <div class="form-group">
                                    <label>Phone</label>
                                    <input type="tel" value="+1 (555) 123-4567">
                                </div>
                            </div>
                            <div class="form-group">
                                <label>Bio</label>
                                <textarea rows="4" placeholder="Tell us about yourself..."></textarea>
                            </div>
                            <button type="submit" class="btn">Update Profile</button>
                        </form>
                    </div>
                </div>

                <!-- Analytics Content -->
                <div id="analytics-content" class="content-section">
                    <div class="content-header">
                        <h1>Analytics</h1>
                        <p>Track your performance and growth metrics.</p>
                    </div>
                    <div class="content-body">
                        <div class="stats-grid">
                            <div class="stat-card">
                                <h3>24,567</h3>
                                <p>Page Views</p>
                            </div>
                            <div class="stat-card">
                                <h3>3,456</h3>
                                <p>Unique Visitors</p>
                            </div>
                            <div class="stat-card">
                                <h3>12.3%</h3>
                                <p>Bounce Rate</p>
                            </div>
                            <div class="stat-card">
                                <h3>4.2min</h3>
                                <p>Avg. Session</p>
                            </div>
                        </div>
                        <div style="height: 300px; background: #f8f9fa; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-top: 20px;">
                            <p>📊 Analytics Chart Placeholder</p>
                        </div>
                    </div>
                </div>

                <!-- Messages Content -->
                <div id="messages-content" class="content-section">
                    <div class="content-header">
                        <h1>Messages</h1>
                        <p>Communicate with your team and clients.</p>
                    </div>
                    <div class="content-body">
                        <div class="activity-feed">
                            <div class="activity-item">
                                <div class="activity-icon">💬</div>
                                <div>
                                    <strong>Sarah Johnson</strong>
                                    <p>Hey, can we discuss the project timeline?</p>
                                    <small>2 hours ago</small>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">💬</div>
                                <div>
                                    <strong>Mike Chen</strong>
                                    <p>The design looks great! Ready for development.</p>
                                    <small>5 hours ago</small>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">💬</div>
                                <div>
                                    <strong>Emma Wilson</strong>
                                    <p>Meeting scheduled for tomorrow at 2 PM.</p>
                                    <small>1 day ago</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Projects Content -->
                <div id="projects-content" class="content-section">
                    <div class="content-header">
                        <h1>Projects</h1>
                        <p>Manage your active and completed projects.</p>
                    </div>
                    <div class="content-body">
                        <div class="stats-grid">
                            <div class="stat-card">
                                <h3>Website Redesign</h3>
                                <p>In Progress - 75% Complete</p>
                            </div>
                            <div class="stat-card">
                                <h3>Mobile App</h3>
                                <p>Planning - 25% Complete</p>
                            </div>
                            <div class="stat-card">
                                <h3>Brand Identity</h3>
                                <p>Completed - 100% Complete</p>
                            </div>
                            <div class="stat-card">
                                <h3>E-commerce Store</h3>
                                <p>On Hold - 50% Complete</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Team Content -->
                <div id="team-content" class="content-section">
                    <div class="content-header">
                        <h1>Team</h1>
                        <p>Manage your team members and their roles.</p>
                    </div>
                    <div class="content-body">
                        <div class="activity-feed">
                            <div class="activity-item">
                                <div class="activity-icon">👤</div>
                                <div>
                                    <strong>John Doe</strong>
                                    <p>Senior Developer - Team Lead</p>
                                    <small>john.doe@example.com</small>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">👤</div>
                                <div>
                                    <strong>Sarah Johnson</strong>
                                    <p>UI/UX Designer</p>
                                    <small>sarah.johnson@example.com</small>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">👤</div>
                                <div>
                                    <strong>Mike Chen</strong>
                                    <p>Frontend Developer</p>
                                    <small>mike.chen@example.com</small>
                                </div>
                            </div>
                            <div class="activity-item">
                                <div class="activity-icon">👤</div>
                                <div>
                                    <strong>Emma Wilson</strong>
                                    <p>Project Manager</p>
                                    <small>emma.wilson@example.com</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Settings Content -->
                <div id="settings-content" class="content-section">
                    <div class="content-header">
                        <h1>Settings</h1>
                        <p>Configure your account and application preferences.</p>
                    </div>
                    <div class="content-body">
                        <div class="settings-section">
                            <h3>Notifications</h3>
                            <div class="setting-item">
                                <span>Email Notifications</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                            <div class="setting-item">
                                <span>Push Notifications</span>
                                <div class="toggle-switch" onclick="toggleSetting(this)"></div>
                            </div>
                            <div class="setting-item">
                                <span>SMS Notifications</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                        </div>
                        <div class="settings-section">
                            <h3>Privacy</h3>
                            <div class="setting-item">
                                <span>Profile Visibility</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                            <div class="setting-item">
                                <span>Activity Status</span>
                                <div class="toggle-switch" onclick="toggleSetting(this)"></div>
                            </div>
                            <div class="setting-item">
                                <span>Data Collection</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                        </div>
                        <div class="settings-section">
                            <h3>Security</h3>
                            <div class="setting-item">
                                <span>Two-Factor Authentication</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                            <div class="setting-item">
                                <span>Login Alerts</span>
                                <div class="toggle-switch active" onclick="toggleSetting(this)"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>

    <script>
        // Page Navigation
        function showMainPage(pageId) {
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            document.getElementById(pageId).classList.add('active');
        }

        // Show Sign Up Page
        function showSignUp() {
            showMainPage('signup-page');
        }

        // Show Login Page
        function showLogin() {
            showMainPage('login-page');
        }

        // Login Form Handler
        document.getElementById('login-form').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Simple validation (in real app, this would be server-side)
            if (email && password) {
                // Create a new page transition effect
                createPageTransition('verification-page');
            } else {
                alert('Please fill in all fields');
            }
        });

        // Sign Up Form Handler
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('signup-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const name = document.getElementById('signup-name').value;
                const email = document.getElementById('signup-email').value;
                const password = document.getElementById('signup-password').value;
                const confirmPassword = document.getElementById('signup-confirm-password').value;
                
                // Validation
                if (!name || !email || !password || !confirmPassword) {
                    alert('Please fill in all fields');
                    return;
                }
                
                if (password !== confirmPassword) {
                    alert('Passwords do not match');
                    return;
                }
                
                if (password.length < 6) {
                    alert('Password must be at least 6 characters long');
                    return;
                }
                
                // Create account success - go to verification
                createPageTransition('verification-page');
            });
        });

        // Create smooth page transition
        function createPageTransition(targetPageId) {
            const currentPage = document.querySelector('.page.active');
            const targetPage = document.getElementById(targetPageId);
            
            // Add fade out effect to current page
            currentPage.style.opacity = '0';
            currentPage.style.transform = 'translateY(-20px)';
            
            setTimeout(() => {
                currentPage.classList.remove('active');
                targetPage.classList.add('active');
                targetPage.style.opacity = '0';
                targetPage.style.transform = 'translateY(20px)';
                
                // Animate in new page
                setTimeout(() => {
                    targetPage.style.opacity = '1';
                    targetPage.style.transform = 'translateY(0)';
                }, 50);
            }, 300);
        }

        // Verification Code Handler
        const codeInputs = document.querySelectorAll('.code-digit');
        codeInputs.forEach((input, index) => {
            input.addEventListener('input', function() {
                if (this.value.length === 1 && index < codeInputs.length - 1) {
                    codeInputs[index + 1].focus();
                }
            });
            
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Backspace' && this.value === '' && index > 0) {
                    codeInputs[index - 1].focus();
                }
            });
        });

        function verifyCode() {
            const code = Array.from(codeInputs).map(input => input.value).join('');
            if (code.length === 6) {
                // Create transition to main app
                createPageTransition('main-app');
            } else {
                alert('Please enter the complete verification code');
            }
        }

        // Dashboard Navigation
        function showPage(pageId) {
            // Update active nav link
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Update content
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
                section.style.display = 'none';
            });
            
            const targetContent = document.getElementById(pageId + '-content');
            if (targetContent) {
                targetContent.style.display = 'block';
                targetContent.classList.add('active');
            }
            
            // Close mobile menu
            closeMobileMenu();
        }

        // Mobile Menu Toggle
        function toggleMobileMenu() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('mobile-open');
        }

        function closeMobileMenu() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.remove('mobile-open');
        }

        // Settings Toggle
        function toggleSetting(element) {
            element.classList.toggle('active');
        }

        // Logout
        function logout() {
            if (confirm('Are you sure you want to logout?')) {
                createPageTransition('login-page');
                // Reset forms
                document.getElementById('login-form').reset();
                document.getElementById('signup-form').reset();
                // Clear verification code
                codeInputs.forEach(input => input.value = '');
                // Reset navigation
                document.querySelectorAll('.nav-link').forEach(link => {
                    link.classList.remove('active');
                });
                document.querySelector('.nav-link[onclick="showPage(\'dashboard\')"]').classList.add('active');
                setTimeout(() => {
                    showPage('dashboard');
                }, 500);
            }
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            // Show dashboard by default
            showPage('dashboard');
            
            // Add some interactive animations
            const statCards = document.querySelectorAll('.stat-card');
            statCards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-10px) scale(1.02)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(-5px) scale(1)';
                });
            });
            
            // Add loading animation to buttons
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('click', function() {
                    this.innerHTML = '<span>Loading...</span>';
                    setTimeout(() => {
                        this.innerHTML = this.getAttribute('data-original-text') || 'Submit';
                    }, 2000);
                });
            });
            
            // Store original button text
            buttons.forEach(button => {
                button.setAttribute('data-original-text', button.innerHTML);
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            const sidebar = document.getElementById('sidebar');
            const menuBtn = document.querySelector('.mobile-menu-btn');
            
            if (sidebar.classList.contains('mobile-open') && 
                !sidebar.contains(e.target) && 
                !menuBtn.contains(e.target)) {
                closeMobileMenu();
            }
        });

        // Add smooth scrolling for better UX
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Dynamic greeting based on time
        function updateGreeting() {
            const hour = new Date().getHours();
            const dashboardHeader = document.querySelector('#dashboard-content .content-header h1');
            
            if (hour < 12) {
                dashboardHeader.textContent = 'Good Morning!';
            } else if (hour < 17) {
                dashboardHeader.textContent = 'Good Afternoon!';
            } else {
                dashboardHeader.textContent = 'Good Evening!';
            }
        }

        // Call greeting function
        updateGreeting();

        // Add some real-time updates simulation
        setInterval(function() {
            const statCards = document.querySelectorAll('.stat-card h3');
            statCards.forEach(card => {
                if (card.textContent.includes(')) {
                    const currentValue = parseInt(card.textContent.replace(/[^0-9]/g, ''));
                    const newValue = currentValue + Math.floor(Math.random() * 10);
                    card.textContent = ' + newValue.toLocaleString();
                }
            });
        }, 10000); // Update every 10 seconds

        // Add keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey || e.metaKey) {
                switch(e.key) {
                    case '1':
                        e.preventDefault();
                        showPage('dashboard');
                        break;
                    case '2':
                        e.preventDefault();
                        showPage('profile');
                        break;
                    case '3':
                        e.preventDefault();
                        showPage('analytics');
                        break;
                    case '4':
                        e.preventDefault();
                        showPage('messages');
                        break;
                    case '5':
                        e.preventDefault();
                        showPage('projects');
                        break;
                    case '6':
                        e.preventDefault();
                        showPage('team');
                        break;
                    case '7':
                        e.preventDefault();
                        showPage('settings');
                        break;
                }
            }
        });
    </script>
</body>
</html>
