#!/bin/bash

FILES = $(shell grep -Po "^logo_[^:]+(?=:)" Makefile)

all:
	make $(FILES)

logo_plain.svg: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-text-to-path; export-plain-svg; export-do;" $<

logo_sepia.png: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-dpi:192; export-do;" $<

logo_sepia.eps: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-do;" $<

logo_sepia.pdf: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-text-to-path; export-do;" $<

logo_white.png: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-id:layer1; export-id-only; export-background:white; export-dpi:192; export-do;" $<

logo_white.eps: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-id:layer1; export-id-only; export-background:white; export-do;" $<

logo_white.pdf: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-id:layer1; export-id-only; export-background:white; export-do;" $<

logo_transparent.png: logo.svg Makefile
	inkscape --actions="export-filename:$@; export-area-page; export-id:layer1; export-id-only; export-dpi:192; export-do;" $<

