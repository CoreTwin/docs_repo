#!/bin/bash

set -e

echo "🏗️ Building update-docs-system package..."
echo "📁 Current directory: $(pwd)"
echo ""

print_status() {
    echo "✅ $1"
}

print_warning() {
    echo "⚠️  $1"
}

print_error() {
    echo "❌ $1"
}

if [ ! -f "pyproject.toml" ]; then
    print_error "pyproject.toml not found!"
    echo "💡 Please run this script from the root of the update-docs repository"
    exit 1
fi

print_status "Found pyproject.toml"

echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/
print_status "Previous builds cleaned"

echo "📦 Building package..."
if python -m build; then
    print_status "Package built successfully"
else
    print_error "Failed to build package"
    exit 1
fi

echo ""
echo "📋 Package contents:"
if [ -f dist/*.tar.gz ]; then
    tar -tzf dist/*.tar.gz | head -20
    echo "..."
    echo "Total files: $(tar -tzf dist/*.tar.gz | wc -l)"
else
    print_warning "No .tar.gz file found in dist/"
fi

echo ""
echo "📊 Package sizes:"
ls -lh dist/

echo ""
print_status "Package built successfully!"
echo ""
echo "📋 Next steps:"
echo "  1. Test installation: pip install dist/*.whl"
echo "  2. Publish to PyPI: twine upload dist/*"
echo "  3. Test from PyPI: pip install update-docs-system"
echo ""
echo "🔍 To verify package contents:"
echo "  unzip -l dist/*.whl"
