Title: Reading mri metadata from MRI scan (dcm) files
Date: 2016-01-27
Tags: python

I recently read on [HackerNews](https://news.ycombinator.com) about a man who published his MRI scans on github. Turns out he didn't clear them of any metadata and you can actually get his name and other personally identifying information (PII) from those files. While I'm not going to publish that, I was interested in how to do this. Turns out it's super easy to read, using the [pydicom](http://www.pydicom.org/) library.

To read, simply `pip install pydicom`. Then:

```
import dicom
ds = dicom.read_file(file_path)
print ds
```

You'll get a very long output, some sample lines (cleared of PII):
```
(0008, 103e) Series Description                  LO: '----'
(0008, 1040) Institutional Department Name       LO: 'CRYSTAL SPRING MEDICAL OFFICE BUILDING'
(0008, 1048) Physician(s) of Record              PN: '----'
(0008, 1060) Name of Physician(s) Reading Study  PN: '----'
(0008, 1090) Manufacturer's Model Name           LO: 'Sonata'
```

If you wish to remove the metadata from the dcm file, you can simply:
```
ds.clear()
ds.save_as(file_path)
```

Full code at [github](https://github.com/angelga/python_samples/blob/master/mri_metadata.py).
