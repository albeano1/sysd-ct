# Project variables
PROJECT_NAME = counter_service
VERSION = 2.0.0
BUILD_DIR = build
DIST_DIR = dist
DEB_NAME = $(PROJECT_NAME)-v$(VERSION).deb

# Default target
.PHONY: all
all: build

# Build the binary using PyInstaller
.PHONY: build
build:
	rm -rf $(BUILD_DIR) $(DIST_DIR)  # Clean old builds
	mkdir -p $(BUILD_DIR) $(DIST_DIR)  
	pyinstaller --onefile --name=$(PROJECT_NAME) $(PROJECT_NAME).py --distpath $(DIST_DIR)

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

# Lint the Debian package
.PHONY: lint-deb
lint-deb: build-deb
	lintian $(DEB_NAME)

# Build Debian package
.PHONY: build-deb
build-deb: build
	bash deb-build.sh