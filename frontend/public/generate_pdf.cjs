const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Load the HTML file
  const filePath = `file://${path.resolve(__dirname, 'legal-policy.html')}`;
  await page.goto(filePath, { waitUntil: 'networkidle0' });
  
  // Generate PDF
  await page.pdf({
    path: path.resolve(__dirname, 'legal-policy.pdf'),
    format: 'A4',
    margin: {
      top: '20mm',
      right: '20mm',
      bottom: '20mm',
      left: '20mm'
    },
    printBackground: true
  });
  
  await browser.close();
  console.log('PDF generated successfully with Puppeteer.');
})();
