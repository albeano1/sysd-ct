# Project variables
PROJECT_NAME = counter-service  # Use hyphen (-) for the project name
SCRIPT_NAME = counter_service.py  # Use the actual script filename (with underscore)
VERSION = 2.0.0
BUILD_DIR = build
DIST_DIR = dist
DEB_NAME = $(PROJECT_NAME)-v$(VERSION).deb

# Default target
.PHONY: all
all: build

# Install dependencies
.PHONY: install-deps
install-deps:
	@if ! command -v pyinstaller >/dev/null 2>&1; then \
		echo "PyInstaller not found. Installing..."; \
		pip install pyinstaller; \
	fi

# Build the binary using PyInstaller
.PHONY: build
build: install-deps
	rm -rf $(BUILD_DIR) $(DIST_DIR)  # Clean old builds
	mkdir -p $(BUILD_DIR) $(DIST_DIR)  
	pyinstaller --onefile --name=$(PROJECT_NAME) $(SCRIPT_NAME) --distpath $(DIST_DIR)

# Run the program
.PHONY: run
run: build
	./$(DIST_DIR)/$(PROJECT_NAME)

# Clean generated files
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR) __pycache__ *.spec $(PROJECT_NAME)-v*.deb

# Unit Testing
.PHONY: test
test:
	@echo "Running unit tests..."
	PYTHONPATH=$(PWD) pytest tests/

# Build Debian package
.PHONY: build-deb
build-deb: build
	@if [ ! -f deb-build.sh ]; then \
		echo "Error: deb-build.sh script not found!"; \
		exit 1; \
	fi
	chmod +x deb-build.sh  # Ensure the script is executable
	./deb-build.sh

# Lint the Debian package
.PHONY: lint-deb
lint-deb: build-deb
	@if ! command -v lintian >/dev/null 2>&1; then \
		echo "Error: lintian is not installed. Please install it using 'sudo apt-get install lintian'."; \
		exit 1; \
	fi
	@echo "Linting Debian package: $(DEB_NAME)"
	lintian "$(DEB_NAME)"