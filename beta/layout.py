# layout.py
def serve_base_html(active_section):
    return f"""
        <!DOCTYPE html>
        <html data-theme="light">
        <head>
            <title>My Portfolio - {active_section.title()}</title>
            <link href="https://cdn.jsdelivr.net/npm/daisyui@4.7.2/dist/full.min.css" rel="stylesheet" type="text/css" />
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
        </head>
        <body class="bg-base-100">
            <!-- Navigation -->
            <nav class="navbar bg-base-200 shadow-lg sticky top-0 z-50">
                <div class="container mx-auto px-4">
                    <div class="flex justify-between items-center py-4 w-full">
                        <a href="/" class="text-xl font-bold">My Portfolio</a>
                        <div class="flex gap-4">
                            <a href="/admin" class="btn btn-ghost {active_section == 'home' and 'btn-active'}">
                                <i class="fa-solid fa-crown mr-2"></i>Admin
                            </a>
                           <button onclick="toggleTheme()" class="btn btn-ghost">
                                <i class="fas fa-moon"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>
    """

def serve_footer():
    return """
            <script>
                function toggleTheme() {
                    const html = document.documentElement;
                    const currentTheme = html.getAttribute('data-theme');
                    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                    html.setAttribute('data-theme', newTheme);
                }
            </script>
        </body>
        </html>
    """
