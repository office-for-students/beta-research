import logging
import os

import course_docs


def main():
    logging.info('Python HTTP trigger function processed a request.')

    xml_filename = './kis.xml'
    course_docs.create_course_docs(xml_filename)


main()
