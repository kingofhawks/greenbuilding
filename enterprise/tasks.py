def html2pdf(pdf_url, pdf_root, project_id):
    from subprocess import call
    call(["phantomjs", "e:\Workspace\greenbuilding\static\js\html2pdf.js", pdf_url, pdf_root, project_id])

if __name__ == '__main__':
    html2pdf('E:/workspace/greenbuilding/media/submission/', 'test')
