import unittest
import sys
import pandas as pds
import pdsti

class PDSAggTest(unittest.TestCase):

    def setUp(self):
        self.tidata= 'testdatati.csv'
        self.tidframe = pds.read_csv(self.tidata)

    if __name__ == '__main__':
        unittest.main()
#############################################
#              TI
#############################################
#TI#DIST
    def testcountdistti(self):
        self.assertEqual(
            pdsti.countdist(self.tidframe, 'prob'),
            [0, 0, 225000.0, ]

        )
    def testsumdistti(self):
        self.assertEqual()
    def testmaxdistti(self):
        self.assertEqual()
    def testmindistti(self):
        self.assertEqual()

#TI#RANGE
    def testcountrangti(self):
        self.assertEqual()
    def testsumrangti(self):
        self.assertEqual()
    def testmaxrangti(self):
        self.assertEqual()
    def testminrangti(self):
        self.assertEqual()

#TI#EXPECTED
    def testcountexpectedti(self):
        self.assertEqual()
    def testsumexpectedti(self):
        self.assertEqual()
    def testmaxexpectedti(self):
        self.assertEqual()
    def testminexpectedti(self):
        self.assertEqual()
############################################
#               BID
############################################
#BID#DIST
    def testcountdistbid(self):
        self.assertEqual()
    def testsumdistbid(self):
        self.assertEqual()
    def testmaxdistbid(self):
        self.assertEqual()
    def testmindistbid(self):
        self.assertEqual()

#BID#RANGE
    def testcountrangbid(self):
        self.assertEqual()
    def testsumrangbid(self):
        self.assertEqual()
    def testmaxrangbid(self):
        self.assertEqual()
    def testminrangbid(self):
        self.assertEqual()

#BID#EXPECTED
    def testcountexpectedbid(self):
        self.assertEqual()
    def testsumexpectedbid(self):
        self.assertEqual()
    def testmaxexpectedbid(self):
        self.assertEqual()
    def testminexpectedbid(self):
        self.assertEqual()
