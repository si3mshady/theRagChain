// Function to combine documents into a single string
function combine_documents(documents) {
    return documents.map((doc) => (doc.pageContent)).join('\n\n');
}


export {combine_documents}