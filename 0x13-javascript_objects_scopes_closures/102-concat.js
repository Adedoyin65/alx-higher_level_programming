#!/usr/bin/node
const fs = require('fs');

// Get command line arguments
const [, , file1Path, file2Path, destPath] = process.argv;

// Function to concatenate files
const concatFiles = (file1, file2, destFile) => {
  try {
    // Read the contents of the first file
    const file1Content = fs.readFileSync(file1, 'utf8');

    // Read the contents of the second file
    const file2Content = fs.readFileSync(file2, 'utf8');

    // Concatenate the contents of the files
    const concatenatedContent = file1Content + file2Content;

    // Write the concatenated content to the destination file
    fs.writeFileSync(destFile, concatenatedContent);

    console.log(`Files  and  concatenated successfully to .`);
  } catch (err) {
    console.error('Error concatenating files:', err);
  }
};

// Call the concatFiles function with the provided file paths
concatFiles(file1Path, file2Path, destPath);
