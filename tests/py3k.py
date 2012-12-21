#!/usr/bin/env python
# -*- coding: latin-1 -*-

"Basic example to test py3k conversion"

import sys
from fpdf import FPDF
    
pdf = FPDF()
# compression is also supported in py3k version
pdf.compress = True
pdf.add_page()
# unicode is not yet supported in py3k version, use windows-1252 standards font
pdf.set_font('Arial','',14)  
pdf.ln(10)
pdf.write(5, 'hello world %s áéíóúüñ' % sys.version)

fn='py3k.pdf'
pdf.output(fn,'F')
import os
try:
    os.startfile(fn)
except:
    os.system("evince %s" % fn)
