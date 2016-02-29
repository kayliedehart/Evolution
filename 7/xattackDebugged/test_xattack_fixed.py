# Automated unit tests for a xattack test harness for Evolution game
import unittest
import xattack_fixed
from attack import species
from attack import trait

class TestXAttack(unittest.TestCase):
  def setUp(self):
    tester_xattack = xattack.TestHarness()
    case_0357_6344_1_in = [[["food",3], ["body",3], ["population",3], ["traits",[]]], [["food",3], ["body",3], ["population",3], ["traits",["carnivore"]]], false, false]
    case_0357_6344_1_out = true

    case_0357_6344_5_in = [[["food",1], ["body",3], ["population",5], ["traits",["symbiosis"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], [["food",2], ["body",5], ["population",5], ["traits",[]]], false]
    case_0357_6344_5_out = true

    case_0357_6344_8_in = [[["food",1], ["body",3], ["population",4], ["traits",["herding"]]], [["food",2], ["body",4], ["population",5], ["traits",["carnivore"]]], false, false]
    case_0357_6344_8_out = true

    case_0357_6344_9_in =[[["food",1], ["body",3], ["population",4], ["traits",["herding"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], false, false]
    case_0357_6344_9_out = false

    case_0357_6344_11_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], [["food",2], ["body",3], ["population",4], ["traits",["warning-call"]]], false]
    case_0357_6344_11_out = false

    case_0357_6344_12_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore", "ambush"]]], false, false]
    case_0357_6344_12_out = true

    case_0357_6344_13_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore", "ambush"]]], false, [["food",2], ["body",3], ["population",4], ["traits",["warning-call"]]]]
    case_0357_6344_13_out = true

    case_0357_6344_14_in = [[["food",2], ["body",3], ["population",4], ["traits",["burrowing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], false, false]
    case_0357_6344_14_out = true

    case_0357_6344_15_in = [[["food",3], ["body",3], ["population",3], ["traits",["burrowing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], false, false]
    case_0357_6344_15_out = false

    case_0357_6344_16_in = [[["food",2], ["body",3], ["population",4], ["traits",["climbing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], false, false]
    case_0357_6344_16_out = false

    case_0623_8070_1_in = [
                            [["food", 1], ["body", 0], ["population", 1], ["traits", []]],
                            [["food", 1], ["body", 0], ["population", 1], ["traits", ["carnivore"]]],
                            false,
                            false
                          ]
    case_0623_8070_1_out = true

    case_1073_6112_3_in = [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["carnivore"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ]
                          ]
    case_1073_6112_3_out = true

    case_1073_6112_4_in = [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["climbing"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["carnivore", "climbing"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ]
                          ]
    case_1073_6112_4_out = true

    case_1073_6112_5_in =[
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["cooperation", "fertile", "ambush"]]
                          ],
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["carnivore"]]
                          ],
                          false,
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["warning-call", "horns"]]
                          ]
                        ]
    case_1073_6112_5_out = false

    case_2657_7498_1_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], false, false ]
    case_2657_7498_1_out = true

    case_2657_7498_2_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["burrowing", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], false, false ]
    case_2657_7498_2_out = false

    case_2657_7498_3_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["warning-call", "carnivore"]] ], false ]
    case_2657_7498_3_out = false

    case_2657_7498_4_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["warning-call", "carnivore"]] ], false ]
    case_2657_7498_4_out = true

    case_2657_7498_5_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",[]] ], false ]
    case_2657_7498_5_out = true

    case_2657_7498_6_in = [ [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["symbiosis", "carnivore"]] ],
                            [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["ambush", "carnivore"]] ],
                            [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",[]] ], false ]
    case_2657_7498_6_out = true

    case_2657_7498_8_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["climbing"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], false, [ ["food",3], ["body",4], ["population",3], ["traits",[]] ] ]
    case_2657_7498_8_out = false

    case_2657_7498_9_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["climbing"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["climbing", "carnivore"]] ], false, [ ["food",3], ["body",4], ["population",3], ["traits",[]] ] ]
    case_2657_7498_9_out = true

    case_2657_7498_10_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["hard-shell", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], false, false ]
    case_2657_7498_10_out = false

    case_2657_7498_12_in = [ [ ["food",3], ["body",4], ["population",3], ["traits",["hard-shell", "carnivore"]] ], [ ["food",3], ["body",7], ["population",3], ["traits",["ambush", "carnivore"]] ], false, false ]
    case_2657_7498_12_out = false

    case_2657_7498_14_in = [ [ ["food",3], ["body",4], ["population",3], ["traits",[]] ], [ ["food",1], ["body",7], ["population",1], ["traits",["carnivore"]] ], [ ["food",1], ["body",7], ["population",1], ["traits",["warning-call"]] ], false ]
    case_2657_7498_14_out = false

    case_9634_1853_1_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_1_out = true

    case_9634_1853_3_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], false]
    case_9634_1853_3_out = false

    case_9634_1853_4_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]]]
    case_9634_1853_4_out = false

    case_9634_1853_5_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore", "ambush"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], false]
    case_9634_1853_5_out = true

    case_9634_1853_7_in = [[["food", 6], ["body", 0], ["population", 6], ["traits", ["burrowing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_7_out = false

    case_9634_1853_8_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["climbing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_8_out = false

    case_9634_1853_9_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["climbing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore", "climbing"]]], false, false]
    case_9634_1853_9_out = true

    case_9634_1853_10_in =[[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_10_out = false

    case_9634_1853_11_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 3], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_11_out = false

    case_9634_1853_13_in =[[["food", 0], ["body", 0], ["population", 1], ["traits", ["herding"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_13_out = false

    case_9634_1853_14_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["herding"]]], [["food", 0], ["body", 0], ["population", 2], ["traits", ["carnivore"]]], false, false]
    case_9634_1853_14_out = true

    case_9634_1853_18_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["symbiosis"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], false, [["food", 0], ["body", 0], ["population", 1], ["traits", []]]]
    case_9634_1853_18_out = true

    case_9634_1853_20_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 0], ["population", 3], ["traits", ["carnivore", "pack-hunting"]]], false, false]
    case_9634_1853_20_out = false

    matthias_1_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,false]
    matthias_1_out = true

    matthias_2_in = [[["food",1],["body",1],["population",1],["traits",["burrowing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,false]
    matthias_2_out = false

    matthias_3_in = [[["food",3],["body",1],["population",4],["traits",["burrowing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,false]
    matthias_3_out = true

    matthias_4_in = [[["food",3],["body",1],["population",4],["traits",["climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,false]
    matthias_4_out = false

    matthias_5_in = [[["food",3],["body",1],["population",4],["traits",["climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","climbing"]]],false,false]
    matthias_5_out = true

    matthias_6_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,false]
    matthias_6_out = false

    matthias_7_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",7],["population",3],["traits",["carnivore"]]],false,false]
    matthias_7_out = true

    matthias_8_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","pack-hunting"]]],false,false]
    matthias_8_out = true

    matthias_9_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],false]
    matthias_9_out = false

    matthias_10_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],false,[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    matthias_10_out = false

    matthias_11_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    matthias_11_out = false

    matthias_12_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush"]]],false,[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    matthias_12_out = true

    matthias_13_in = [[["food",2],["body",2],["population",2],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],false]
    matthias_13_out = true

    matthias_14_in = [[["food",2],["body",2],["population",2],["traits",["hard-shell","climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],false]
    matthias_14_out = false


  def tearDown(self):
    del case_0357_6344_1_in
    del case_0357_6344_1_out
    del case_0357_6344_5_in
    del case_0357_6344_5_out
    del case_0357_6344_8_in
    del case_0357_6344_8_out
    del case_0357_6344_9_in
    del case_0357_6344_9_out
    del case_0357_6344_11_in
    del case_0357_6344_11_out
    del case_0357_6344_12_in
    del case_0357_6344_12_out
    del case_0357_6344_12_in
    del case_0357_6344_13_out
    del case_0357_6344_13_in
    del case_0357_6344_13_out
    del case_0357_6344_15_in
    del case_0357_6344_15_out
    del case_0357_6344_16_in
    del case_0357_6344_16_out

    del case_0623_8070_1_in
    del case_0623_8070_1_out

    del case_1073_6112_3_in
    del case_1073_6112_3_out
    del case_1073_6112_4_in
    del case_1073_6112_4_out
    del case_1073_6112_5_in
    del case_1073_6112_5_out

    del case_2657_7498_1_in
    del case_2657_7498_1_out
    del case_2657_7498_2_in
    del case_2657_7498_2_out
    del case_2657_7498_3_in
    del case_2657_7498_3_out
    del case_2657_7498_4_in
    del case_2657_7498_4_out
    del case_2657_7498_5_in
    del case_2657_7498_5_out
    del case_2657_7498_6_in
    del case_2657_7498_6_out
    del case_2657_7498_8_in
    del case_2657_7498_8_out
    del case_2657_7498_9_in
    del case_2657_7498_9_out
    del case_2657_7498_10_in
    del case_2657_7498_10_out
    del case_2657_7498_12_in
    del case_2657_7498_12_out
    del case_2657_7498_14_in
    del case_2657_7498_14_out

    del case_9634_1853_1_in
    del case_9634_1853_1_out
    del case_9634_1853_3_in
    del case_9634_1853_3_out
    del case_9634_1853_4_in
    del case_9634_1853_4_out
    del case_9634_1853_5_in
    del case_9634_1853_5_out
    del case_9634_1853_7_in
    del case_9634_1853_7_out
    del case_9634_1853_8_in
    del case_9634_1853_8_out
    del case_9634_1853_9_in
    del case_9634_1853_9_out
    del case_9634_1853_10_in
    del case_9634_1853_10_out
    del case_9634_1853_11_in
    del case_9634_1853_11_out
    del case_9634_1853_13_in
    del case_9634_1853_13_out
    del case_9634_1853_14_in
    del case_9634_1853_14_out
    del case_9634_1853_18_in
    del case_9634_1853_18_out
    del case_9634_1853_20_in
    del case_9634_1853_20_out

    del matthias_1_in
    del matthias_1_out
    del matthias_2_in
    del matthias_2_out
    del matthias_3_in
    del matthias_3_out
    del matthias_4_in
    del matthias_4_out
    del matthias_5_in
    del matthias_5_out
    del matthias_6_in
    del matthias_6_out
    del matthias_7_in
    del matthias_7_out
    del matthias_8_in
    del matthias_8_out
    del matthias_9_in
    del matthias_9_out
    del matthias_10_in
    del matthias_10_out
    del matthias_11_in
    del matthias_11_out
    del matthias_12_in
    del matthias_12_out
    del matthias_13_in
    del matthias_13_out
    del matthias_14_in
    del matthias_14_out


  def test_0357_6344(self):
    self.assertEqual(tester_xattack.testMethod(case_0357_6344_1_in), case_0357_6344_1_out)


if __name__ == '__main__':
    unittest.main()