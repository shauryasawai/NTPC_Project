from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Welcome to SynergyGrid</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- Tailwind CSS -->
      <script src="https://cdn.tailwindcss.com"></script>
      <!-- Particles.js -->
      <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
      <!-- Google Fonts -->
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
      <style>
        /* Reset and basic setup */
        body {
          margin: 0;
          padding: 0;
          background-color: #0f0f0f;
          font-family: 'Poppins', sans-serif;
          position: relative;
          overflow-x: hidden;
          min-height: 100vh;
        }
        /* Fullscreen particle background */
        #particles-js {
          position: absolute;
          width: 100%;
          height: 100%;
          z-index: 0;
          top: 0;
          left: 0;
        }
        /* Vignette overlay for extra depth */
        body::after {
          content: "";
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background: radial-gradient(ellipse at center, rgba(0,0,0,0) 0%, #000 100%);
          opacity: 0.4;
          z-index: -1;
        }
        /* Centering container */
        .container {
          position: relative;
          z-index: 1;
          display: flex;
          align-items: center;
          justify-content: center;
          min-height: 100vh;
          padding: 1rem;
        }
        /* Glassmorphism-style card with fade-in & hover effect */
        .card {
          background: rgba(255, 255, 255, 0.1);
          border-radius: 15px;
          box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
          backdrop-filter: blur(8px);
          -webkit-backdrop-filter: blur(8px);
          border: 1px solid rgba(255, 255, 255, 0.18);
          padding: 2rem;
          max-width: 400px;
          text-align: center;
          animation: fadeInUp 1s ease-out;
          transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
          transform: scale(1.02) rotate(0.5deg);
          box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
        }
        @keyframes fadeInUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        /* Gradient header with shimmer effect */
        h2 {
          background: linear-gradient(45deg, #1D4ED8, #2563EB, #3B82F6);
          background-size: 200%;
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          font-size: 2.5rem;
          margin-bottom: 1.5rem;
          animation: shimmer 3s ease-in-out infinite;
        }
        @keyframes shimmer {
          0% {
            background-position: 0% 50%;
          }
          50% {
            background-position: 100% 50%;
          }
          100% {
            background-position: 0% 50%;
          }
        }
        /* Stylish navigation buttons */
        .btn {
          background: linear-gradient(45deg, #1D4ED8, #2563EB);
          color: #fff;
          padding: 0.75rem 1.5rem;
          border-radius: 8px;
          text-decoration: none;
          font-weight: 600;
          transition: transform 0.2s, box-shadow 0.2s;
          display: inline-block;
          margin: 0.5rem 0;
        }
        .btn:hover {
          transform: translateY(-3px) scale(1.05);
          box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
        }
      </style>
    </head>
    <body>
      <div id="particles-js"></div>
      <div class="container">
        <div class="card">
          <h2>Welcome to SynergyGrid</h2>
          <div class="space-y-4">
            <p><a class="btn" href="/forecasting/">Go to Energy Forecasting</a></p>
            <p><a class="btn" href="/maintenance/">Go to Equipment Maintenance Predictions</a></p>
            <p><a class="btn" href="/dashboard/">Visit Dashboard</a></p>
            <p><a class="btn" href="/users/register/">Users/Role</a></p>
          </div>
        </div>
      </div>
      <script>
        /* Initialize particles.js for a dynamic, interactive background */
        particlesJS("particles-js", {
          "particles": {
            "number": {
              "value": 100,
              "density": {
                "enable": true,
                "value_area": 800
              }
            },
            "color": { "value": "#ffffff" },
            "shape": {
              "type": "circle",
              "stroke": { "width": 0, "color": "#000000" },
              "polygon": { "nb_sides": 5 }
            },
            "opacity": {
              "value": 0.5,
              "random": false
            },
            "size": {
              "value": 3,
              "random": true
            },
            "line_linked": {
              "enable": true,
              "distance": 150,
              "color": "#ffffff",
              "opacity": 0.4,
              "width": 1
            },
            "move": {
              "enable": true,
              "speed": 4,
              "direction": "none",
              "random": false,
              "straight": false,
              "out_mode": "out"
            }
          },
          "interactivity": {
            "detect_on": "canvas",
            "events": {
              "onhover": {
                "enable": true,
                "mode": "repulse"
              },
              "onclick": {
                "enable": true,
                "mode": "push"
              },
              "resize": true
            },
            "modes": {
              "repulse": { "distance": 100, "duration": 0.4 },
              "push": { "particles_nb": 4 }
            }
          },
          "retina_detect": true
        });
      </script>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('forecasting/', include('energy_forecasting.urls')),
    path('maintenance/', include('predictive_maintenance.urls')),
    path('dashboard/', include('dashboard.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

