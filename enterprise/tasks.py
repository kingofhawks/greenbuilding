def html2pdf(pdf_root, project_id):
    from subprocess import call
    call(["phantomjs", "e:\Workspace\greenbuilding\static\js\html2pdf.js", pdf_root, project_id])

if __name__ == '__main__':
    html2pdf('E:/workspace/greenbuilding/media/submission/', 'test')
