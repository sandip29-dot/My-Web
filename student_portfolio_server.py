import http.server
import socketserver

# The port you want your local server to run on
PORT = 8000

# The complete HTML, CSS, and JS embedded as a Python string
jls_extract_var = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sandip Bhowmik| Student & Developer</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Tailwind Configuration -->
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        gray: {
                            50: '#f9fafb',
                            100: '#f3f4f6',
                            200: '#e5e7eb',
                            800: '#1f2937',
                            900: '#111827',
                            950: '#030712',
                        }
                    }
                }
            }
        }
    </script>
    
    <!-- Fonts: Arial -->
    
    <style>
        body {
            font-family: 'Inter', sans-serif;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        
        /* Subtle fade-in animation */
        .fade-in {
            animation: fadeIn 0.8s ease-out forwards;
            opacity: 0;
            transform: translateY(10px);
        }
        
        .delay-100 { animation-delay: 100ms; }
        .delay-200 { animation-delay: 200ms; }
        .delay-300 { animation-delay: 300ms; }

        @keyframes fadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Canvas Styling for Paint Effect */
        #paint-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none; /* Allows clicking through the canvas */
            z-index: 0; /* Keeps it behind the main content */
            opacity: 0.8;
        }

        /* Ensure content stays above the canvas */
        nav, main, footer {
            position: relative;
            z-index: 10;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 dark:bg-gray-950 dark:text-gray-100 min-h-screen flex flex-col antialiased selection:bg-gray-300 dark:selection:bg-gray-700 selection:text-black dark:selection:text-white relative">

    <!-- Interactive Paint Canvas -->
    <canvas id="paint-canvas"></canvas>

    <!-- Navigation -->
    <nav class="w-full max-w-3xl mx-auto px-6 py-8 flex justify-between items-center fade-in">
        <a href="#" class="font-medium text-lg tracking-tight hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
            sandip.bhowmik
        </a>
        <button id="theme-toggle" class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors focus:outline-none focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-700" aria-label="Toggle Dark Mode">
            <!-- Moon Icon (Dark Mode) -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="hidden dark:block">
                <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>
            </svg>
            <!-- Sun Icon (Light Mode) -->
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="block dark:hidden">
                <circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>
            </svg>
        </button>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow w-full max-w-3xl mx-auto px-6 py-12 flex flex-col gap-20">
        
        <!-- Hero Section -->
        <section class="flex flex-col gap-6 fade-in delay-100">
            <div>
                <h1 class="text-4xl sm:text-5xl font-semibold tracking-tight mb-3">Hi, I'm Sandip.</h1>
                <p class="text-xl sm:text-2xl text-gray-600 dark:text-gray-400 font-light">
                    Curious about numbers, technology and the designs that make them come alive.
                </p>
            </div>
            
            <p class="text-base text-gray-600 dark:text-gray-400 leading-relaxed max-w-2xl">
                I'm a Second year student at University of Delhi. I enjoy turning complex problems into simple, beautiful, and intuitive designs. When I'm not coding, you'll find me reading sci-fi or exploring local coffee shops.
            </p>

            <!-- Quick Links -->
            <div class="flex flex-wrap gap-4 mt-2">
                <a href="#" class="flex items-center gap-2 px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-700 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>
                    Resume
                </a>
                <a href="#" class="flex items-center gap-2 px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-700 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.2c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>
                    GitHub
                </a>
                <a href="#" class="flex items-center gap-2 px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-700 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
                    LinkedIn
                </a>
            </div>
        </section>

        <!-- Current Focus -->
        <section class="fade-in delay-200">
            <h2 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-6">Currently Learning</h2>
            <div class="flex flex-wrap gap-3">
                <span class="px-3 py-1 border border-gray-200 dark:border-gray-800 rounded-md text-sm">Mathematics</span>
                <span class="px-3 py-1 border border-gray-200 dark:border-gray-800 rounded-md text-sm">Computer Science</span>
                <span class="px-3 py-1 border border-gray-200 dark:border-gray-800 rounded-md text-sm">Machine Learning Basics</span>
                <span class="px-3 py-1 border border-gray-200 dark:border-gray-800 rounded-md text-sm">Design</span>
            </div>
        </section>

        <!-- Projects Section -->
        <section class="fade-in delay-300">
            <h2 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-6">Selected Projects</h2>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <!-- Project Card 1 -->
                <a href="#" class="group block p-6 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-2xl hover:border-gray-300 dark:hover:border-gray-700 transition-all hover:shadow-sm">
                    <div class="flex justify-between items-start mb-4">
                        <h3 class="font-medium text-lg">StudyTimer</h3>
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400 group-hover:text-gray-900 dark:group-hover:text-gray-100 transition-colors"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">A minimalist Pomodoro timer web app built to help students track their study sessions without distractions.</p>
                    <div class="text-xs text-gray-500 dark:text-gray-500 font-medium">HTML • Tailwind • JS</div>
                </a>

                <!-- Project Card 2 -->
                <a href="#" class="group block p-6 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-2xl hover:border-gray-300 dark:hover:border-gray-700 transition-all hover:shadow-sm">
                    <div class="flex justify-between items-start mb-4">
                        <h3 class="font-medium text-lg">CourseScraper</h3>
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400 group-hover:text-gray-900 dark:group-hover:text-gray-100 transition-colors"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">A Python script that aggregates available courses from the university portal and notifies users of open seats.</p>
                    <div class="text-xs text-gray-500 dark:text-gray-500 font-medium">Python • BeautifulSoup</div>
                </a>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="fade-in delay-300 mb-12">
            <h2 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-6">Get in Touch</h2>
            <p class="text-gray-600 dark:text-gray-400 mb-4">
                Whether you want to discuss a project, talk about tech, or just say hi, my inbox is always open.
            </p>
            <a href="mailto:hello@example.com" class="inline-flex items-center gap-2 text-gray-900 dark:text-white font-medium hover:underline underline-offset-4 decoration-gray-300 dark:decoration-gray-700 transition-all">
                hello@example.com 
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
            </a>
        </section>

    </main>

    <!-- Footer -->
    <footer class="w-full max-w-3xl mx-auto px-6 py-8 border-t border-gray-200 dark:border-gray-800 flex justify-between items-center text-sm text-gray-500 dark:text-gray-400">
        <p>&copy; <span id="year"></span> Sandip Bhowmik.</p>
        <p>Built with Curiosity.</p>
    </footer>

    <script>
        const canvas = document.getElementById('paint-canvas');
        const ctx = canvas.getContext('2d');

        // Resize canvas to fit window
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Paint brush variables
        const points = [];
        // A playful 4-color palette (Neon Pink, Cyan, Yellow, Purple)
        const colors = ['#FF10F0', '#00FFFF', '#FFD700', '#8A2BE2'];
        let colorIndex = 0;
        
        const mouse = { x: null, y: null };
        let isMoving = false;
        let timeout;

        window.addEventListener('mousemove', (e) => {
            mouse.x = e.x;
            mouse.y = e.y;
            isMoving = true;
            
            // Add new point with current color
            points.push({ 
                x: mouse.x, 
                y: mouse.y, 
                age: 0,
                color: colors[colorIndex]
            });

            // Cycle colors slowly based on number of points
            if (points.length % 15 === 0) {
                colorIndex = (colorIndex + 1) % colors.length;
            }

            clearTimeout(timeout);
            timeout = setTimeout(() => isMoving = false, 100);
        });

        function animatePaint() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            if (points.length > 0) {
                ctx.lineJoin = 'round';
                ctx.lineCap = 'round';
                
                for (let i = 0; i < points.length; i++) {
                    const p = points[i];
                    p.age += 1; // Increase age to handle fading
                    
                    // Remove points older than ~4-5 seconds (approx 240-300 frames at 60fps)
                    if (p.age > 250) {
                        points.splice(i, 1);
                        i--;
                        continue;
                    }

                    if (i > 0) {
                        const prevP = points[i - 1];
                        
                        // Calculate thickness and opacity based on age (fades out as it gets older)
                        const lifePercentage = 1 - (p.age / 250);
                        ctx.lineWidth = 15 * lifePercentage; 
                        
                        // Set color with varying opacity
                        ctx.strokeStyle = `${p.color}${Math.floor(lifePercentage * 255).toString(16).padStart(2, '0')}`;
                        
                        // Smooth bezier curve between points for a brush effect
                        ctx.beginPath();
                        ctx.moveTo(prevP.x, prevP.y);
                        
                        // Control point for curve
                        const xc = (prevP.x + p.x) / 2;
                        const yc = (prevP.y + p.y) / 2;
                        ctx.quadraticCurveTo(prevP.x, prevP.y, xc, yc);
                        
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animatePaint);
        }
        
        // Start animation loop
        animatePaint();

        // Set Current Year in Footer
        document.getElementById('year').textContent = new Date().getFullYear();

        // Dark Mode Logic
        const themeToggleBtn = document.getElementById('theme-toggle');
        const htmlElement = document.documentElement;

        // Check for saved user preference, if any, on load of the website
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            htmlElement.classList.add('dark');
        } else {
            htmlElement.classList.remove('dark');
        }

        // Listen for toggle button click
        themeToggleBtn.addEventListener('click', function() {
            // if set via local storage previously
            if (localStorage.getItem('color-theme')) {
                if (localStorage.getItem('color-theme') === 'light') {
                    htmlElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                } else {
                    htmlElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                }
            // if NOT set via local storage previously
            } else {
                if (htmlElement.classList.contains('dark')) {
                    htmlElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    htmlElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            }
        });
    </script>
</body>
</html>
"""
HTML_CONTENT = jls_extract_var

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP Request Handler that serves our embedded HTML content
    when the root URL ('/') is accessed.
    """
    def do_GET(self):
        # Serve the HTML content for the root path
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Write the HTML string as utf-8 encoded bytes
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        else:
            # Fallback to standard request handling for any other paths (e.g., if you add images later)
            super().do_GET()

# Create the server object
with socketserver.TCPServer(("", PORT), PortfolioHandler) as httpd:
    print(f"✅ Server started!")
    print(f"🚀 Open your web browser and go to: http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    try:
        # Keep the server running until interrupted
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Graceful shutdown on Ctrl+C
        print("\n🛑 Shutting down server...")
        httpd.server_close()