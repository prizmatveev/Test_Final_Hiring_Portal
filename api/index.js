let app;
let connectDB;
let isConnected = false;

module.exports = async (req, res) => {
  // Dynamically import ES modules to bypass Vercel ESM syntax errors
  if (!app) {
    app = (await import('../backend/src/app.js')).default;
    connectDB = (await import('../backend/src/config/db.js')).default;
  }

  // Only connect to DB if not already connected
  if (!isConnected) {
    try {
      await connectDB();
      isConnected = true;
    } catch (err) {
      console.error('Failed to connect to database in serverless function:', err);
      return res.status(500).json({ error: 'Database connection failed' });
    }
  }

  // Delegate request to Express app
  return app(req, res);
};
