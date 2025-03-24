#!/bin/bash

set -e

PROJECT_NAME="counter-service"  # Use hyphen (-) instead of underscore (_) in project name
VERSION="2.0.0"
DIST_DIR="dist"
DEB_NAME="${PROJECT_NAME}-v${VERSION}.deb"  # Use hyphen (-) instead of underscore (_) in version
INSTALL_DIR="/usr/local/bin"

# Create package structure
PKG_DIR="deb_pkg"
mkdir -p $PKG_DIR/DEBIAN
mkdir -p $PKG_DIR/$INSTALL_DIR
mkdir -p $PKG_DIR/lib/systemd/system

# Copy binary from the dist directory
cp $DIST_DIR/$PROJECT_NAME $PKG_DIR/$INSTALL_DIR/

# Create control file
cat <<EOF > $PKG_DIR/DEBIAN/control
Package: $PROJECT_NAME
Version: $VERSION
Architecture: all
Maintainer: Sean Nickerson
Description: A simple counter service for logging timestamps.
EOF

# Copy systemd service file
cp counter.service $PKG_DIR/lib/systemd/system/

# Build the package
dpkg-deb --build $PKG_DIR $DEB_NAME

# Cleanup
rm -rf $PKG_DIR

echo "Debian package built: $DEB_NAME"