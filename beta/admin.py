# admin.py
from layout import serve_base_html, serve_footer
from card_modal import serve_card_modal

def serve_admin_panel():
    content = serve_base_html('admin_panel')
    content += """
        <div class="min-h-screen bg-base-200 py-12">
            <div class="container mx-auto px-4">
                <div class="text-center mb-8">
                    <h1 class="text-5xl font-bold mb-4">Admin Dashboard</h1>
                    <p class="text-lg mb-8">Manage your Islamic Books Collection</p>
                    
                    <!-- Admin Actions Section -->
                    <div class="max-w-2xl mx-auto mb-12">
                        <div class="flex justify-center gap-4 mb-8">
                            <button onclick="document.getElementById('add-book-modal').showModal()" class="btn btn-primary">
                                <i class="fas fa-plus mr-2"></i>Add New Book
                            </button>
                            <button class="btn btn-accent">
                                <i class="fas fa-download mr-2"></i>Export Data
                            </button>
                        </div>
                        
                        <!-- Search and Filter -->
                        <div class="join w-full">
                            <input type="text" placeholder="Search books to manage..." class="input input-bordered join-item w-full" />
                            <button class="btn btn-primary join-item">
                                <i class="fas fa-search"></i>
                            </button>
                        </div>
                    </div>
                </div>
                
                <!-- Books Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Example Book Card with Admin Controls -->
                    <div class="card bg-base-100 shadow-xl">
                        <figure class="px-6 pt-6 relative">
                            <img src="/api/placeholder/300/200" alt="Quran" class="rounded-xl shadow" />
                            <div class="absolute top-8 right-8 flex gap-2">
                                <button onclick="document.getElementById('edit-book-modal').showModal()" 
                                        class="btn btn-circle btn-sm btn-primary">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button onclick="document.getElementById('delete-book-modal').showModal()" 
                                        class="btn btn-circle btn-sm btn-error">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </figure>
                        <div class="card-body">
                            <div class="flex justify-between items-start">
                                <h2 class="card-title text-2xl">The Noble Quran</h2>
                                <div class="badge badge-primary">
                                    <i class="fas fa-book-quran mr-2"></i>Quran
                                </div>
                            </div>
                            <p class="text-sm text-gray-600">Translation & Commentary</p>
                            <div class="flex items-center gap-2 mt-2">
                                <span class="font-semibold">Author:</span>
                                <span>Dr. Muhammad Muhsin Khan</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="font-semibold">Status:</span>
                                <div class="badge badge-success">Published</div>
                            </div>
                            <div class="divider my-2"></div>
                            <div class="space-y-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold">Downloads:</span>
                                    <span>1,234</span>
                                </div>
                                <div class="flex flex-wrap gap-2">
                                    <a href="#" class="btn btn-sm btn-primary">
                                        <i class="fas fa-download mr-2"></i>Main Download
                                    </a>
                                    <a href="#" class="btn btn-sm">
                                        <i class="fas fa-book-reader mr-2"></i>Preview
                                    </a>
                                    <div class="dropdown dropdown-end">
                                        <label tabindex="0" class="btn btn-sm">
                                            <i class="fas fa-ellipsis-v"></i>
                                        </label>
                                        <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
                                            <li><a href="#"><i class="fas fa-link mr-2"></i>Alt Source 1</a></li>
                                            <li><a href="#"><i class="fas fa-link mr-2"></i>Alt Source 2</a></li>
                                            <li><a href="#" class="text-error"><i class="fas fa-exclamation-triangle mr-2"></i>Report Links</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="card-actions justify-end mt-4">
                                <button class="btn btn-outline btn-sm">
                                    <i class="fas fa-eye mr-2"></i>View Statistics
                                </button>
                                <button class="btn btn-outline btn-sm" onclick="checkLinks(this)">
                                    <i class="fas fa-link mr-2"></i>Check Links
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Book Modal -->
        <dialog id="add-book-modal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg mb-4">Add New Book</h3>
                <form method="dialog" class="space-y-4">
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Book Title</span>
                        </label>
                        <input type="text" placeholder="Enter book title" class="input input-bordered w-full" />
                    </div>
                    
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Author</span>
                        </label>
                        <input type="text" placeholder="Enter author name" class="input input-bordered w-full" />
                    </div>
                    
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Category</span>
                        </label>
                        <select class="select select-bordered w-full">
                            <option disabled selected>Select a category</option>
                            <option>Quran</option>
                            <option>Hadith</option>
                            <option>Fiqh</option>
                            <option>Seerah</option>
                            <option>General</option>
                        </select>
                    </div>
                    
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Book Cover</span>
                        </label>
                        <input type="file" class="file-input file-input-bordered w-full" />
                    </div>
                    
                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Description</span>
                        </label>
                        <textarea class="textarea textarea-bordered" placeholder="Enter book description"></textarea>
                    </div>

                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Download URL</span>
                            <span class="label-text-alt text-info">
                                <i class="fas fa-circle-info"></i> Direct download link for the book
                            </span>
                        </label>
                        <div class="join w-full">
                            <input type="url" placeholder="Enter download URL" class="input input-bordered join-item w-full" />
                            <button class="btn btn-primary join-item" onclick="validateURL(this)">
                                <i class="fas fa-link"></i>
                            </button>
                        </div>
                    </div>

                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Preview URL</span>
                            <span class="label-text-alt text-info">
                                <i class="fas fa-circle-info"></i> Link to preview/read online
                            </span>
                        </label>
                        <div class="join w-full">
                            <input type="url" placeholder="Enter preview URL" class="input input-bordered join-item w-full" />
                            <button class="btn btn-primary join-item" onclick="validateURL(this)">
                                <i class="fas fa-link"></i>
                            </button>
                        </div>
                    </div>

                    <div class="form-control">
                        <label class="label">
                            <span class="label-text">Alternative Download Sources</span>
                        </label>
                        <div id="alt-downloads" class="space-y-2">
                            <div class="join w-full">
                                <input type="url" placeholder="Alternative download URL" class="input input-bordered join-item w-full" />
                                <button class="btn btn-error join-item" onclick="removeAltDownload(this)">
                                    <i class="fas fa-minus"></i>
                                </button>
                            </div>
                        </div>
                        <button class="btn btn-outline btn-sm mt-2" onclick="addAltDownload()">
                            <i class="fas fa-plus mr-2"></i>Add Alternative Source
                        </button>
                    </div>
                    
                    <div class="modal-action">
                        <button class="btn btn-primary">Add Book</button>
                        <button class="btn">Cancel</button>
                    </div>
                </form>
            </div>
        </dialog>

        <!-- Edit Book Modal -->
        <dialog id="edit-book-modal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg mb-4">Edit Book</h3>
                <form method="dialog" class="space-y-4">
                    <!-- Similar fields as Add Book Modal but pre-filled -->
                    <div class="modal-action">
                        <button class="btn btn-primary">Save Changes</button>
                        <button class="btn">Cancel</button>
                    </div>
                </form>
            </div>
        </dialog>

        <!-- Delete Confirmation Modal -->
        <dialog id="delete-book-modal" class="modal">
            <div class="modal-box">
                <h3 class="font-bold text-lg text-error">Delete Book</h3>
                <p class="py-4">Are you sure you want to delete this book? This action cannot be undone.</p>
                <div class="modal-action">
                    <button class="btn btn-error">Delete</button>
                    <button class="btn">Cancel</button>
                </div>
            </div>
        </dialog>
    """
    content += serve_footer()
    
    # Add JavaScript for modal and admin functionality
    content += """
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                // Initialize any necessary admin functionality
                
                // Handle file uploads
                const fileInput = document.querySelector('.file-input');
                if (fileInput) {
                    fileInput.addEventListener('change', function(e) {
                        // Handle file upload preview
                        const file = e.target.files[0];
                        if (file) {
                            // Add preview functionality
                        }
                    });
                }
                
                // Handle form submissions
                const forms = document.querySelectorAll('form');
                forms.forEach(form => {
                    form.addEventListener('submit', function(e) {
                        e.preventDefault();
                        // Add form submission handling
                    });
                });
            });

            // URL validation and management
            function validateURL(button) {
                const input = button.previousElementSibling;
                try {
                    new URL(input.value);
                    // Add visual feedback
                    button.innerHTML = '<i class="fas fa-check"></i>';
                    button.classList.add('btn-success');
                    setTimeout(() => {
                        button.innerHTML = '<i class="fas fa-link"></i>';
                        button.classList.remove('btn-success');
                    }, 2000);
                } catch {
                    // Add error feedback
                    button.innerHTML = '<i class="fas fa-xmark"></i>';
                    button.classList.add('btn-error');
                    setTimeout(() => {
                        button.innerHTML = '<i class="fas fa-link"></i>';
                        button.classList.remove('btn-error');
                    }, 2000);
                }
            }

            // Alternative download sources management
            function addAltDownload() {
                const container = document.getElementById('alt-downloads');
                const newDownload = document.createElement('div');
                newDownload.className = 'join w-full';
                newDownload.innerHTML = `
                    <input type="url" placeholder="Alternative download URL" class="input input-bordered join-item w-full" />
                    <button class="btn btn-error join-item" onclick="removeAltDownload(this)">
                        <i class="fas fa-minus"></i>
                    </button>
                `;
                container.appendChild(newDownload);
            }

            function removeAltDownload(button) {
                button.parentElement.remove();
            }

            // Link checker functionality
            async function checkLinks(button) {
                const originalText = button.innerHTML;
                button.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Checking...';
                button.disabled = true;

                try {
                    // Simulate checking links (replace with actual API call)
                    await new Promise(resolve => setTimeout(resolve, 2000));
                    
                    // Show results in a toast or modal
                    const toast = document.createElement('div');
                    toast.className = 'toast toast-end';
                    toast.innerHTML = `
                        <div class="alert alert-success">
                            <i class="fas fa-check-circle"></i>
                            <span>All links are working!</span>
                        </div>
                    `;
                    document.body.appendChild(toast);
                    setTimeout(() => toast.remove(), 3000);
                } catch (error) {
                    // Handle errors
                    const toast = document.createElement('div');
                    toast.className = 'toast toast-end';
                    toast.innerHTML = `
                        <div class="alert alert-error">
                            <i class="fas fa-exclamation-circle"></i>
                            <span>Some links might be broken!</span>
                        </div>
                    `;
                    document.body.appendChild(toast);
                    setTimeout(() => toast.remove(), 3000);
                }

                button.innerHTML = originalText;
                button.disabled = false;
            }
        </script>
    """
    return content
