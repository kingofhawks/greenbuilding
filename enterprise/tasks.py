def html2pdf(pdf_url, pdf_root, project_id):
    from subprocess import call
    call(["phantomjs", "D:\Workspace\greenbuilding\static\js\html2pdf.js", pdf_url, pdf_root, project_id])

if __name__ == '__main__':
    html2pdf('http://localhost:8000/enterprise/projects/1/submission/pdf/',
             'D:/workspace/greenbuilding/media/submission/', '1')
