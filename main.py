from app import app

if __name__ == '__main__':
    # Enhanced configuration for VSCode compatibility
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
