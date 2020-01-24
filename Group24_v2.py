class ShovelComplete:
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        self.ID = Identity
        self.LT = LT
        self.Q = Q
        self.Period = Period
        self.GrossRequirements = GS
        self.ScheduledReceipts = SR
        self.OnHandFromPriorPeriod = OHFPP
        self.NetRequirements = NR
        self.TimePhasedNetRequirements = TPNR
        self.PlannedOrderRelases = POR
        self.PlannedOrderDelivery = POD
        

class TopHandle_13122(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class TopHandle_457(TopHandle_13122):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Bracelet(TopHandle_13122):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class TopHandle_129(Bracelet):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class TopHandle_1118(Bracelet):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class ScoopShaft(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Shaft(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Nail(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Rivet(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class ScoopAssembly(ShovelComplete):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Scoop(ScoopAssembly):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


class Blade(ScoopAssembly):
    def __init__(self, Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD):
        super().__init__(Identity, LT, Q, Period, GS, SR, OHFPP, NR, TPNR, POR, POD)


objectOfITEM_1605 = ShovelComplete(1605, 1, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                   [0, 0, 0, 60, 100, 0, 50, 0, 30, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [30, 30, 30, 30, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_13122 = TopHandle_13122(13122, 1, 40, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 70, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 40, 20, 20, 10, 10, 20, 20],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_048 = ScoopShaft(48, 3, 30, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [30, 30, 30, 0, 20, 20, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_118 = Shaft(118, 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 50, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 50, 20, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_314 = ScoopAssembly(314, 1, 50, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 50, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 20, 20, 70, 20, 20, 40, 40],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_062 = Nail(62, 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [50, 50, 50, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_14127 = Rivet(14127, 1, 100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [60, 60, 60, 40, 40, 40, 40, 40, 20, 20],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

objectOfITEM_2142 = Scoop(2142, 2, 100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [80, 80, 30, 30, 30, 30, 30, 80, 80, 80],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

objectOfITEM_019 = Blade(19, 2, 50, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 40, 0, 0, 0, 0, 0],
                         [50, 50, 0, 0, 0, 40, 40, 40, 40, 40],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_457 = TopHandle_457(457, 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 20, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 20, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
objectOfITEM_11495 = Bracelet(457, 1, 50, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [120, 120, 120, 40, 40, 0, 0, 10, 10, 10],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

objectOfITEM_129 = Bracelet(129, 4, 40, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 100, 0, 0],
                            [0, 0, 0, 0, 0, 0, 30, 30, 130, 130],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

objectOfITEM_1118 = Bracelet(1118, 3, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [30, 30, 30, 30, 30, 30, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


# 1 ITEM
def ITEM_1605():
    for i in range(len(objectOfITEM_1605.Period)):
        if objectOfITEM_1605.GrossRequirements[i] != 0 and objectOfITEM_1605.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1605.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_1605.OnHandFromPriorPeriod[i] > objectOfITEM_1605.GrossRequirements[i]:
                objectOfITEM_1605.NetRequirements[i] = 0
                objectOfITEM_1605.OnHandFromPriorPeriod[i + 1] = objectOfITEM_1605.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_1605.GrossRequirements[i]
                if objectOfITEM_1605.Q == 1:
                    objectOfITEM_1605.PlannedOrderRelases = objectOfITEM_1605.TimePhasedNetRequirements
                    objectOfITEM_1605.PlannedOrderDelivery = objectOfITEM_1605.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                        j += objectOfITEM_1605.Q
                        if j >= objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                            objectOfITEM_1605.PlannedOrderRelases[i - objectOfITEM_1605.LT] = j
                            objectOfITEM_1605.PlannedOrderDelivery[i] = objectOfITEM_1605.PlannedOrderRelases[
                                i - objectOfITEM_1605.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_1605.NetRequirements[i] = objectOfITEM_1605.GrossRequirements[i] - \
                                                       objectOfITEM_1605.OnHandFromPriorPeriod[i]
                objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT] = \
                    objectOfITEM_1605.NetRequirements[i]
                if objectOfITEM_1605.Q == 1:
                    objectOfITEM_1605.PlannedOrderRelases = objectOfITEM_1605.TimePhasedNetRequirements
                    objectOfITEM_1605.PlannedOrderDelivery = objectOfITEM_1605.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                        j += objectOfITEM_1605.Q
                        if j >= objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                            objectOfITEM_1605.PlannedOrderRelases[i - objectOfITEM_1605.LT] = j
                            objectOfITEM_1605.PlannedOrderDelivery[i] = objectOfITEM_1605.PlannedOrderRelases[
                                i - objectOfITEM_1605.LT]
                            break
                continue
        elif objectOfITEM_1605.GrossRequirements[i] != 0 and objectOfITEM_1605.ScheduledReceipts[i] != 0 and \
                objectOfITEM_1605.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_1605.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_1605.GrossRequirements[i] - objectOfITEM_1605.ScheduledReceipts[i])
            if objectOfITEM_1605.OnHandFromPriorPeriod[i] > objectOfITEM_1605.GrossRequirements[i]:
                objectOfITEM_1605.NetRequirements[i] = 0
                objectOfITEM_1605.OnHandFromPriorPeriod[i + 1] = objectOfITEM_1605.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_1605.GrossRequirements[i]
                if objectOfITEM_1605.Q == 1:
                    objectOfITEM_1605.PlannedOrderRelases = objectOfITEM_1605.TimePhasedNetRequirements
                    objectOfITEM_1605.PlannedOrderDelivery = objectOfITEM_1605.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                        j += objectOfITEM_1605.Q
                        if j >= objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                            objectOfITEM_1605.PlannedOrderRelases[i - objectOfITEM_1605.LT] = j
                            objectOfITEM_1605.PlannedOrderDelivery[i] = objectOfITEM_1605.PlannedOrderRelases[
                                i - objectOfITEM_1605.LT]
                            break
                continue

            else:
                objectOfITEM_1605.NetRequirements[i + 1] = objectOfITEM_1605.GrossRequirements[i + 1] - \
                                                           objectOfITEM_1605.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT] = \
                    objectOfITEM_1605.NetRequirements[i]
                if objectOfITEM_1605.Q == 1:
                    objectOfITEM_1605.PlannedOrderRelases = objectOfITEM_1605.TimePhasedNetRequirements
                    objectOfITEM_1605.PlannedOrderDelivery = objectOfITEM_1605.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                        j += objectOfITEM_1605.Q
                        if j >= objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                            objectOfITEM_1605.PlannedOrderRelases[i - objectOfITEM_1605.LT] = j
                            objectOfITEM_1605.PlannedOrderDelivery[i] = objectOfITEM_1605.PlannedOrderRelases[
                                i - objectOfITEM_1605.LT]
                            break
                continue


        elif objectOfITEM_1605.GrossRequirements[i] == 0 and objectOfITEM_1605.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1605.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_1605.GrossRequirements[i] == 0 and objectOfITEM_1605.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1605.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_1605.NetRequirements[i] = 0

        elif objectOfITEM_1605.GrossRequirements[i] != 0 and objectOfITEM_1605.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1605.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_1605.NetRequirements[i] = objectOfITEM_1605.GrossRequirements[i] - \
                                                   objectOfITEM_1605.OnHandFromPriorPeriod[i]
            objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT] = objectOfITEM_1605.NetRequirements[i]
            if objectOfITEM_1605.Q == 1:
                objectOfITEM_1605.PlannedOrderRelases = objectOfITEM_1605.TimePhasedNetRequirements
                objectOfITEM_1605.PlannedOrderDelivery = objectOfITEM_1605.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                    j += objectOfITEM_1605.Q
                    if j >= objectOfITEM_1605.TimePhasedNetRequirements[i - objectOfITEM_1605.LT]:
                        objectOfITEM_1605.PlannedOrderRelases[i - objectOfITEM_1605.LT] = j
                        objectOfITEM_1605.PlannedOrderDelivery[i] = objectOfITEM_1605.PlannedOrderRelases[
                            i - objectOfITEM_1605.LT]
                        break
                    else:
                        continue
            continue
        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_1605.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_1605.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_1605.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_1605.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_1605.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_1605.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_1605.PlannedOrderDelivery)

    objectOfITEM_13122.GrossRequirements = objectOfITEM_1605.PlannedOrderRelases


# 2 ITEM
def ITEM_13122():
    for i in range(len(objectOfITEM_13122.Period)):
        if objectOfITEM_13122.GrossRequirements[i] != 0 and objectOfITEM_13122.ScheduledReceipts[i] == 0 and \
                objectOfITEM_13122.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_13122.OnHandFromPriorPeriod[i] > objectOfITEM_13122.GrossRequirements[i]:
                objectOfITEM_13122.NetRequirements[i] = 0
                objectOfITEM_13122.OnHandFromPriorPeriod[i + 1] = objectOfITEM_13122.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_13122.GrossRequirements[i]
                if objectOfITEM_13122.Q == 1:
                    objectOfITEM_13122.PlannedOrderRelases = objectOfITEM_13122.TimePhasedNetRequirements
                    objectOfITEM_13122.PlannedOrderDelivery = objectOfITEM_13122.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                        j += objectOfITEM_13122.Q
                        if j >= objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                            objectOfITEM_13122.PlannedOrderRelases[i - objectOfITEM_13122.LT] = j
                            objectOfITEM_13122.PlannedOrderDelivery[i] = objectOfITEM_13122.PlannedOrderRelases[
                                i - objectOfITEM_13122.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_13122.NetRequirements[i] = objectOfITEM_13122.GrossRequirements[i] - \
                                                        objectOfITEM_13122.OnHandFromPriorPeriod[i]
                objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT] = \
                    objectOfITEM_13122.NetRequirements[i]
                if objectOfITEM_13122.Q == 1:
                    objectOfITEM_13122.PlannedOrderRelases = objectOfITEM_13122.TimePhasedNetRequirements
                    objectOfITEM_13122.PlannedOrderDelivery = objectOfITEM_13122.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                        j += objectOfITEM_13122.Q
                        if j >= objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                            objectOfITEM_13122.PlannedOrderRelases[i - objectOfITEM_13122.LT] = j
                            objectOfITEM_13122.PlannedOrderDelivery[i] = objectOfITEM_13122.PlannedOrderRelases[
                                i - objectOfITEM_13122.LT]
                            break
                        else:
                            continue
                continue
        elif objectOfITEM_13122.GrossRequirements[i] != 0 and objectOfITEM_13122.ScheduledReceipts[i] != 0 and \
                objectOfITEM_13122.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_13122.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_13122.GrossRequirements[i] - objectOfITEM_13122.ScheduledReceipts[i])
            if objectOfITEM_13122.OnHandFromPriorPeriod[i] > objectOfITEM_13122.GrossRequirements[i]:
                objectOfITEM_13122.NetRequirements[i] = 0
                objectOfITEM_13122.OnHandFromPriorPeriod[i + 1] = objectOfITEM_13122.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_13122.GrossRequirements[i]
                if objectOfITEM_13122.Q == 1:
                    objectOfITEM_13122.PlannedOrderRelases = objectOfITEM_13122.TimePhasedNetRequirements
                    objectOfITEM_13122.PlannedOrderDelivery = objectOfITEM_13122.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                        j += objectOfITEM_13122.Q
                        if j >= objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                            objectOfITEM_13122.PlannedOrderRelases[i - objectOfITEM_13122.LT] = j
                            objectOfITEM_13122.PlannedOrderDelivery[i] = objectOfITEM_13122.PlannedOrderRelases[
                                i - objectOfITEM_13122.LT]
                            break
                        else:
                            continue
                continue

            else:
                objectOfITEM_13122.NetRequirements[i + 1] = objectOfITEM_13122.GrossRequirements[i + 1] - \
                                                            objectOfITEM_13122.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT] = \
                    objectOfITEM_13122.NetRequirements[i]
                if objectOfITEM_13122.Q == 1:
                    objectOfITEM_13122.PlannedOrderRelases = objectOfITEM_13122.TimePhasedNetRequirements
                    objectOfITEM_13122.PlannedOrderDelivery = objectOfITEM_13122.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                        j += objectOfITEM_13122.Q
                        if j >= objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                            objectOfITEM_13122.PlannedOrderRelases[i - objectOfITEM_13122.LT] = j
                            objectOfITEM_13122.PlannedOrderDelivery[i] = objectOfITEM_13122.PlannedOrderRelases[
                                i - objectOfITEM_13122.LT]
                            break
                        else:
                            continue
                continue

        elif objectOfITEM_13122.GrossRequirements[i] == 0 and objectOfITEM_13122.ScheduledReceipts[i] == 0 and \
                objectOfITEM_13122.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_13122.GrossRequirements[i] == 0 and objectOfITEM_13122.ScheduledReceipts[i] == 0 and \
                objectOfITEM_13122.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_13122.NetRequirements[i] = 0

        elif objectOfITEM_13122.GrossRequirements[i] != 0 and objectOfITEM_13122.ScheduledReceipts[i] == 0 and \
                objectOfITEM_13122.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_13122.NetRequirements[i] = objectOfITEM_13122.GrossRequirements[i] - \
                                                    objectOfITEM_13122.OnHandFromPriorPeriod[i]
            objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT] = \
                objectOfITEM_13122.NetRequirements[i]
            if objectOfITEM_13122.Q == 1:
                objectOfITEM_13122.PlannedOrderRelases = objectOfITEM_13122.TimePhasedNetRequirements
                objectOfITEM_13122.PlannedOrderDelivery = objectOfITEM_13122.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                    j += objectOfITEM_13122.Q
                    if j >= objectOfITEM_13122.TimePhasedNetRequirements[i - objectOfITEM_13122.LT]:
                        objectOfITEM_13122.PlannedOrderRelases[i - objectOfITEM_13122.LT] = j
                        objectOfITEM_13122.PlannedOrderDelivery[i] = objectOfITEM_13122.PlannedOrderRelases[
                            i - objectOfITEM_13122.LT]
                        break
                    else:
                        continue
            continue
        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_13122.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_13122.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_13122.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_13122.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_13122.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_13122.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_13122.PlannedOrderDelivery)

    objectOfITEM_048.GrossRequirements = objectOfITEM_1605.PlannedOrderRelases
    objectOfITEM_457.GrossRequirements = objectOfITEM_13122.PlannedOrderRelases

    objectOfITEM_11495.GrossRequirements = objectOfITEM_13122.PlannedOrderRelases


# 3 ITEM
def ITEM_048():
    for i in range(len(objectOfITEM_048.Period)):
        if objectOfITEM_048.GrossRequirements[i] != 0 and objectOfITEM_048.ScheduledReceipts[i] == 0 and \
                objectOfITEM_048.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_048.OnHandFromPriorPeriod[i] > objectOfITEM_048.GrossRequirements[i]:
                objectOfITEM_048.NetRequirements[i] = 0
                objectOfITEM_048.OnHandFromPriorPeriod[i + 1] = objectOfITEM_048.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_048.GrossRequirements[i]
                if objectOfITEM_048.Q == 1:
                    objectOfITEM_048.PlannedOrderRelases = objectOfITEM_048.TimePhasedNetRequirements
                    objectOfITEM_048.PlannedOrderDelivery = objectOfITEM_048.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                        j += objectOfITEM_048.Q
                        if j >= objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                            objectOfITEM_048.PlannedOrderRelases[i - objectOfITEM_048.LT] = j
                            objectOfITEM_048.PlannedOrderDelivery[i] = objectOfITEM_048.PlannedOrderRelases[
                                i - objectOfITEM_048.LT]
                            break
                        else:
                            continue
                continue
            else:
                objectOfITEM_048.NetRequirements[i] = objectOfITEM_048.GrossRequirements[i] - \
                                                      objectOfITEM_048.OnHandFromPriorPeriod[i]
                objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT] = objectOfITEM_048.NetRequirements[
                    i]
                if objectOfITEM_048.Q == 1:
                    objectOfITEM_048.PlannedOrderRelases = objectOfITEM_048.TimePhasedNetRequirements
                    objectOfITEM_048.PlannedOrderDelivery = objectOfITEM_048.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                        j += objectOfITEM_048.Q
                        if j >= objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                            objectOfITEM_048.PlannedOrderRelases[i - objectOfITEM_048.LT] = j
                            objectOfITEM_048.PlannedOrderDelivery[i] = objectOfITEM_048.PlannedOrderRelases[
                                i - objectOfITEM_048.LT]
                            break
                        else:
                            continue
                continue
        elif objectOfITEM_048.GrossRequirements[i] != 0 and objectOfITEM_048.ScheduledReceipts[i] != 0 and \
                objectOfITEM_048.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_048.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_048.GrossRequirements[i] - objectOfITEM_048.ScheduledReceipts[i])
            if objectOfITEM_048.OnHandFromPriorPeriod[i] > objectOfITEM_048.GrossRequirements[i]:
                objectOfITEM_048.NetRequirements[i] = 0
                objectOfITEM_048.OnHandFromPriorPeriod[i + 1] = objectOfITEM_048.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_048.GrossRequirements[i]
                if objectOfITEM_048.Q == 1:
                    objectOfITEM_048.PlannedOrderRelases = objectOfITEM_048.TimePhasedNetRequirements
                    objectOfITEM_048.PlannedOrderDelivery = objectOfITEM_048.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                        j += objectOfITEM_048.Q
                        if j >= objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                            objectOfITEM_048.PlannedOrderRelases[i - objectOfITEM_048.LT] = j
                            objectOfITEM_048.PlannedOrderDelivery[i] = objectOfITEM_048.PlannedOrderRelases[
                                i - objectOfITEM_048.LT]
                            break
                        else:
                            continue
                continue

            else:
                objectOfITEM_048.NetRequirements[i + 1] = objectOfITEM_048.GrossRequirements[i + 1] - \
                                                          objectOfITEM_048.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT] = objectOfITEM_048.NetRequirements[
                    i]
                if objectOfITEM_048.Q == 1:
                    objectOfITEM_048.PlannedOrderRelases = objectOfITEM_048.TimePhasedNetRequirements
                    objectOfITEM_048.PlannedOrderDelivery = objectOfITEM_048.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                        j += objectOfITEM_048.Q
                        if j >= objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                            objectOfITEM_048.PlannedOrderRelases[i - objectOfITEM_048.LT] = j
                            objectOfITEM_048.PlannedOrderDelivery[i] = objectOfITEM_048.PlannedOrderRelases[
                                i - objectOfITEM_048.LT]
                            break
                        else:
                            continue
                continue

        elif objectOfITEM_048.GrossRequirements[i] == 0 and objectOfITEM_048.ScheduledReceipts[i] == 0 and \
                objectOfITEM_048.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_048.GrossRequirements[i] == 0 and objectOfITEM_048.ScheduledReceipts[i] == 0 and \
                objectOfITEM_048.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_048.NetRequirements[i] = 0

        elif objectOfITEM_048.GrossRequirements[i] != 0 and objectOfITEM_048.ScheduledReceipts[i] == 0 and \
                objectOfITEM_048.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_048.NetRequirements[i] = objectOfITEM_048.GrossRequirements[i] - \
                                                  objectOfITEM_048.OnHandFromPriorPeriod[i]
            objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT] = objectOfITEM_048.NetRequirements[i]
            if objectOfITEM_048.Q == 1:
                objectOfITEM_048.PlannedOrderRelases = objectOfITEM_048.TimePhasedNetRequirements
                objectOfITEM_048.PlannedOrderDelivery = objectOfITEM_048.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                    j += objectOfITEM_048.Q
                    if j >= objectOfITEM_048.TimePhasedNetRequirements[i - objectOfITEM_048.LT]:
                        objectOfITEM_048.PlannedOrderRelases[i - objectOfITEM_048.LT] = j
                        objectOfITEM_048.PlannedOrderDelivery[i] = objectOfITEM_048.PlannedOrderRelases[
                            i - objectOfITEM_048.LT]
                        break
                    else:
                        continue
            continue
        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_048.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_048.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_048.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_048.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_048.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_048.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_048.PlannedOrderDelivery)

    objectOfITEM_118.GrossRequirements = objectOfITEM_1605.PlannedOrderRelases


# 4 ITEM
def ITEM_118():
    for i in range(len(objectOfITEM_118.Period)):
        if objectOfITEM_118.GrossRequirements[i] != 0 and objectOfITEM_118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_118.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_118.OnHandFromPriorPeriod[i] > objectOfITEM_118.GrossRequirements[i]:
                objectOfITEM_118.NetRequirements[i] = 0
                objectOfITEM_118.OnHandFromPriorPeriod[i + 1] = objectOfITEM_118.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_118.GrossRequirements[i]
                if objectOfITEM_118.Q == 1:
                    objectOfITEM_118.PlannedOrderRelases = objectOfITEM_118.TimePhasedNetRequirements
                    objectOfITEM_118.PlannedOrderDelivery = objectOfITEM_118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                        j += objectOfITEM_118.Q
                        if j >= objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                            objectOfITEM_118.PlannedOrderRelases[i - objectOfITEM_118.LT] = j
                            objectOfITEM_118.PlannedOrderDelivery[i] = objectOfITEM_118.PlannedOrderRelases[
                                i - objectOfITEM_118.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_118.NetRequirements[i] = objectOfITEM_118.GrossRequirements[i] - \
                                                      objectOfITEM_118.OnHandFromPriorPeriod[i]
                objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT] = objectOfITEM_118.NetRequirements[
                    i]
                if objectOfITEM_118.Q == 1:
                    objectOfITEM_118.PlannedOrderRelases = objectOfITEM_118.TimePhasedNetRequirements
                    objectOfITEM_118.PlannedOrderDelivery = objectOfITEM_118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                        j += objectOfITEM_118.Q
                        if j >= objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                            objectOfITEM_118.PlannedOrderRelases[i - objectOfITEM_118.LT] = j
                            objectOfITEM_118.PlannedOrderDelivery[i] = objectOfITEM_118.PlannedOrderRelases[
                                i - objectOfITEM_118.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_118.GrossRequirements[i] != 0 and objectOfITEM_118.ScheduledReceipts[i] != 0 and \
                objectOfITEM_118.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_118.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_118.GrossRequirements[i] - objectOfITEM_118.ScheduledReceipts[i])
            if objectOfITEM_118.OnHandFromPriorPeriod[i] > objectOfITEM_118.GrossRequirements[i]:
                objectOfITEM_118.NetRequirements[i] = 0
                objectOfITEM_118.OnHandFromPriorPeriod[i + 1] = objectOfITEM_118.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_118.GrossRequirements[i]
                if objectOfITEM_118.Q == 1:
                    objectOfITEM_118.PlannedOrderRelases = objectOfITEM_118.TimePhasedNetRequirements
                    objectOfITEM_118.PlannedOrderDelivery = objectOfITEM_118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                        j += objectOfITEM_118.Q
                        if j >= objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                            objectOfITEM_118.PlannedOrderRelases[i - objectOfITEM_118.LT] = j
                            objectOfITEM_118.PlannedOrderDelivery[i] = objectOfITEM_118.PlannedOrderRelases[
                                i - objectOfITEM_118.LT]
                            break
                        else:
                            continue


            else:
                objectOfITEM_118.NetRequirements[i + 1] = objectOfITEM_118.GrossRequirements[i + 1] - \
                                                          objectOfITEM_118.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT] = objectOfITEM_118.NetRequirements[
                    i]
                if objectOfITEM_118.Q == 1:
                    objectOfITEM_118.PlannedOrderRelases = objectOfITEM_118.TimePhasedNetRequirements
                    objectOfITEM_118.PlannedOrderDelivery = objectOfITEM_118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                        j += objectOfITEM_118.Q
                        if j >= objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                            objectOfITEM_118.PlannedOrderRelases[i - objectOfITEM_118.LT] = j
                            objectOfITEM_118.PlannedOrderDelivery[i] = objectOfITEM_118.PlannedOrderRelases[
                                i - objectOfITEM_118.LT]
                            break
                        else:
                            continue


        elif objectOfITEM_118.GrossRequirements[i] == 0 and objectOfITEM_118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_118.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_118.GrossRequirements[i] == 0 and objectOfITEM_118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_118.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_118.NetRequirements[i] = 0

        elif objectOfITEM_118.GrossRequirements[i] != 0 and objectOfITEM_118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_118.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_118.NetRequirements[i] = objectOfITEM_118.GrossRequirements[i] - \
                                                  objectOfITEM_118.OnHandFromPriorPeriod[i]
            objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT] = objectOfITEM_118.NetRequirements[i]
            if objectOfITEM_118.Q == 1:
                objectOfITEM_118.PlannedOrderRelases = objectOfITEM_118.TimePhasedNetRequirements
                objectOfITEM_118.PlannedOrderDelivery = objectOfITEM_118.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                    j += objectOfITEM_118.Q
                    if j >= objectOfITEM_118.TimePhasedNetRequirements[i - objectOfITEM_118.LT]:
                        objectOfITEM_118.PlannedOrderRelases[i - objectOfITEM_118.LT] = j
                        objectOfITEM_118.PlannedOrderDelivery[i] = objectOfITEM_118.PlannedOrderRelases[
                            i - objectOfITEM_118.LT]
                        break
                    else:
                        continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_118.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_118.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_118.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_118.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_118.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_118.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_118.PlannedOrderDelivery)

    objectOfITEM_314.GrossRequirements = objectOfITEM_1605.PlannedOrderRelases


# 5 ITEM
def ITEM_314():
    for i in range(len(objectOfITEM_314.Period)):
        if objectOfITEM_314.GrossRequirements[i] != 0 and objectOfITEM_314.ScheduledReceipts[i] == 0 and \
                objectOfITEM_314.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_314.OnHandFromPriorPeriod[i] > objectOfITEM_314.GrossRequirements[i]:
                objectOfITEM_314.NetRequirements[i] = 0
                objectOfITEM_314.OnHandFromPriorPeriod[i + 1] = objectOfITEM_314.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_314.GrossRequirements[i]
                if objectOfITEM_314.Q == 1:
                    objectOfITEM_314.PlannedOrderRelases = objectOfITEM_314.TimePhasedNetRequirements
                    objectOfITEM_314.PlannedOrderDelivery = objectOfITEM_314.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                        j += objectOfITEM_314.Q
                        if j >= objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                            objectOfITEM_314.PlannedOrderRelases[i - objectOfITEM_314.LT] = j
                            objectOfITEM_314.PlannedOrderDelivery[i] = objectOfITEM_314.PlannedOrderRelases[
                                i - objectOfITEM_314.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_314.NetRequirements[i] = objectOfITEM_314.GrossRequirements[i] - \
                                                      objectOfITEM_314.OnHandFromPriorPeriod[i]
                objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT] = objectOfITEM_314.NetRequirements[
                    i]
                if objectOfITEM_314.Q == 1:
                    objectOfITEM_314.PlannedOrderRelases = objectOfITEM_314.TimePhasedNetRequirements
                    objectOfITEM_314.PlannedOrderDelivery = objectOfITEM_314.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                        j += objectOfITEM_314.Q
                        if j >= objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                            objectOfITEM_314.PlannedOrderRelases[i - objectOfITEM_314.LT] = j
                            objectOfITEM_314.PlannedOrderDelivery[i] = objectOfITEM_314.PlannedOrderRelases[
                                i - objectOfITEM_314.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_314.GrossRequirements[i] != 0 and objectOfITEM_314.ScheduledReceipts[i] != 0 and \
                objectOfITEM_314.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_314.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_314.GrossRequirements[i] - objectOfITEM_314.ScheduledReceipts[i])
            if objectOfITEM_314.OnHandFromPriorPeriod[i] > objectOfITEM_314.GrossRequirements[i]:
                objectOfITEM_314.NetRequirements[i] = 0
                objectOfITEM_314.OnHandFromPriorPeriod[i + 1] = objectOfITEM_314.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_314.GrossRequirements[i]
                if objectOfITEM_314.Q == 1:
                    objectOfITEM_314.PlannedOrderRelases = objectOfITEM_314.TimePhasedNetRequirements
                    objectOfITEM_314.PlannedOrderDelivery = objectOfITEM_314.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                        j += objectOfITEM_314.Q
                        if j >= objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                            objectOfITEM_314.PlannedOrderRelases[i - objectOfITEM_314.LT] = j
                            objectOfITEM_314.PlannedOrderDelivery[i] = objectOfITEM_314.PlannedOrderRelases[
                                i - objectOfITEM_314.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_314.NetRequirements[i + 1] = objectOfITEM_314.GrossRequirements[i + 1] - \
                                                          objectOfITEM_314.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT] = objectOfITEM_314.NetRequirements[
                    i]
                if objectOfITEM_314.Q == 1:
                    objectOfITEM_314.PlannedOrderRelases = objectOfITEM_314.TimePhasedNetRequirements
                    objectOfITEM_314.PlannedOrderDelivery = objectOfITEM_314.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                        j += objectOfITEM_314.Q
                        if j >= objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                            objectOfITEM_314.PlannedOrderRelases[i - objectOfITEM_314.LT] = j
                            objectOfITEM_314.PlannedOrderDelivery[i] = objectOfITEM_314.PlannedOrderRelases[
                                i - objectOfITEM_314.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_314.GrossRequirements[i] == 0 and objectOfITEM_314.ScheduledReceipts[i] == 0 and \
                objectOfITEM_314.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_314.GrossRequirements[i] == 0 and objectOfITEM_314.ScheduledReceipts[i] == 0 and \
                objectOfITEM_314.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_314.NetRequirements[i] = 0

        elif objectOfITEM_314.GrossRequirements[i] != 0 and objectOfITEM_314.ScheduledReceipts[i] == 0 and \
                objectOfITEM_314.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_314.NetRequirements[i] = objectOfITEM_314.GrossRequirements[i] - \
                                                  objectOfITEM_314.OnHandFromPriorPeriod[i]
            objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT] = objectOfITEM_314.NetRequirements[i]
            if objectOfITEM_314.Q == 1:
                objectOfITEM_314.PlannedOrderRelases = objectOfITEM_314.TimePhasedNetRequirements
                objectOfITEM_314.PlannedOrderDelivery = objectOfITEM_314.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                    j += objectOfITEM_314.Q
                    if j >= objectOfITEM_314.TimePhasedNetRequirements[i - objectOfITEM_314.LT]:
                        objectOfITEM_314.PlannedOrderRelases[i - objectOfITEM_314.LT] = j
                        objectOfITEM_314.PlannedOrderDelivery[i] = objectOfITEM_314.PlannedOrderRelases[
                            i - objectOfITEM_314.LT]
                        break
                    else:
                        continue
        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_314.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_314.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_314.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_314.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_314.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_314.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_314.PlannedOrderDelivery)
    objectOfITEM_2142.GrossRequirements = objectOfITEM_314.PlannedOrderRelases
    objectOfITEM_019.GrossRequirements = objectOfITEM_314.PlannedOrderRelases


# 6 ITEM
def ITEM_062():
    for i in range(len(objectOfITEM_062.Period)):

        objectOfITEM_062.GrossRequirements[i] += (
                objectOfITEM_13122.PlannedOrderRelases[i] * 2 + objectOfITEM_1605.PlannedOrderRelases[i] * 4)

        if objectOfITEM_062.GrossRequirements[i] != 0 and objectOfITEM_062.ScheduledReceipts[i] == 0 and \
                objectOfITEM_062.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_062.OnHandFromPriorPeriod[i] > objectOfITEM_062.GrossRequirements[i]:
                objectOfITEM_062.NetRequirements[i] = 0
                objectOfITEM_062.OnHandFromPriorPeriod[i + 1] = objectOfITEM_062.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_062.GrossRequirements[i]
                if objectOfITEM_062.Q == 1:
                    objectOfITEM_062.PlannedOrderRelases = objectOfITEM_062.TimePhasedNetRequirements
                    objectOfITEM_062.PlannedOrderDelivery = objectOfITEM_062.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                        j += objectOfITEM_062.Q
                        if j >= objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                            objectOfITEM_062.PlannedOrderRelases[i - objectOfITEM_062.LT] = j
                            objectOfITEM_062.PlannedOrderDelivery[i] = objectOfITEM_062.PlannedOrderRelases[
                                i - objectOfITEM_062.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_062.NetRequirements[i] = objectOfITEM_062.GrossRequirements[i] - \
                                                      objectOfITEM_062.OnHandFromPriorPeriod[i]
                objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT] = objectOfITEM_062.NetRequirements[
                    i]
                if objectOfITEM_062.Q == 1:
                    objectOfITEM_062.PlannedOrderRelases = objectOfITEM_062.TimePhasedNetRequirements
                    objectOfITEM_062.PlannedOrderDelivery = objectOfITEM_062.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                        j += objectOfITEM_062.Q
                        if j >= objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                            objectOfITEM_062.PlannedOrderRelases[i - objectOfITEM_062.LT] = j
                            objectOfITEM_062.PlannedOrderDelivery[i] = objectOfITEM_062.PlannedOrderRelases[
                                i - objectOfITEM_062.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_062.GrossRequirements[i] != 0 and objectOfITEM_062.ScheduledReceipts[i] != 0 and \
                objectOfITEM_062.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_062.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_062.GrossRequirements[i] - objectOfITEM_062.ScheduledReceipts[i])
            if objectOfITEM_062.OnHandFromPriorPeriod[i] > objectOfITEM_062.GrossRequirements[i]:
                objectOfITEM_062.NetRequirements[i] = 0
                objectOfITEM_062.OnHandFromPriorPeriod[i + 1] = objectOfITEM_062.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_062.GrossRequirements[i]
                if objectOfITEM_062.Q == 1:
                    objectOfITEM_062.PlannedOrderRelases = objectOfITEM_062.TimePhasedNetRequirements
                    objectOfITEM_062.PlannedOrderDelivery = objectOfITEM_062.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                        j += objectOfITEM_062.Q
                        if j >= objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                            objectOfITEM_062.PlannedOrderRelases[i - objectOfITEM_062.LT] = j
                            objectOfITEM_062.PlannedOrderDelivery[i] = objectOfITEM_062.PlannedOrderRelases[
                                i - objectOfITEM_062.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_062.NetRequirements[i + 1] = objectOfITEM_062.GrossRequirements[i + 1] - \
                                                          objectOfITEM_062.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT] = objectOfITEM_062.NetRequirements[
                    i]
                if objectOfITEM_062.Q == 1:
                    objectOfITEM_062.PlannedOrderRelases = objectOfITEM_062.TimePhasedNetRequirements
                    objectOfITEM_062.PlannedOrderDelivery = objectOfITEM_062.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                        j += objectOfITEM_062.Q
                        if j >= objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                            objectOfITEM_062.PlannedOrderRelases[i - objectOfITEM_062.LT] = j
                            objectOfITEM_062.PlannedOrderDelivery[i] = objectOfITEM_062.PlannedOrderRelases[
                                i - objectOfITEM_062.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_062.GrossRequirements[i] == 0 and objectOfITEM_062.ScheduledReceipts[i] == 0 and \
                objectOfITEM_062.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_062.GrossRequirements[i] == 0 and objectOfITEM_062.ScheduledReceipts[i] == 0 and \
                objectOfITEM_062.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_062.NetRequirements[i] = 0

        elif objectOfITEM_062.GrossRequirements[i] != 0 and objectOfITEM_062.ScheduledReceipts[i] == 0 and \
                objectOfITEM_062.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_062.NetRequirements[i] = objectOfITEM_062.GrossRequirements[i] - \
                                                  objectOfITEM_062.OnHandFromPriorPeriod[i]
            objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT] = objectOfITEM_062.NetRequirements[i]
            if objectOfITEM_062.Q == 1:
                objectOfITEM_062.PlannedOrderRelases = objectOfITEM_062.TimePhasedNetRequirements
                objectOfITEM_062.PlannedOrderDelivery = objectOfITEM_062.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                    j += objectOfITEM_062.Q
                    if j >= objectOfITEM_062.TimePhasedNetRequirements[i - objectOfITEM_062.LT]:
                        objectOfITEM_062.PlannedOrderRelases[i - objectOfITEM_062.LT] = j
                        objectOfITEM_062.PlannedOrderDelivery[i] = objectOfITEM_062.PlannedOrderRelases[
                            i - objectOfITEM_062.LT]
                        break
                    else:
                        continue

        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_062.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_062.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_062.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_062.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_062.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_062.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_062.PlannedOrderDelivery)


# 7 ITEM
def ITEM_14127():
    for i in range(len(objectOfITEM_14127.Period)):
        objectOfITEM_14127.GrossRequirements[i] += (
                objectOfITEM_1605.PlannedOrderRelases[i] * 4 + objectOfITEM_314.PlannedOrderRelases[i] * 6)
        if objectOfITEM_14127.GrossRequirements[i] != 0 and objectOfITEM_14127.ScheduledReceipts[i] == 0 and \
                objectOfITEM_14127.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_14127.OnHandFromPriorPeriod[i] > objectOfITEM_14127.GrossRequirements[i]:
                objectOfITEM_14127.NetRequirements[i] = 0
                objectOfITEM_14127.OnHandFromPriorPeriod[i + 1] = objectOfITEM_14127.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_14127.GrossRequirements[i]
                if objectOfITEM_14127.Q == 1:
                    objectOfITEM_14127.PlannedOrderRelases = objectOfITEM_14127.TimePhasedNetRequirements
                    objectOfITEM_14127.PlannedOrderDelivery = objectOfITEM_14127.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                        j += objectOfITEM_14127.Q
                        if j >= objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                            objectOfITEM_14127.PlannedOrderRelases[i - objectOfITEM_14127.LT] = j
                            objectOfITEM_14127.PlannedOrderDelivery[i] = objectOfITEM_14127.PlannedOrderRelases[
                                i - objectOfITEM_14127.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_14127.NetRequirements[i] = objectOfITEM_14127.GrossRequirements[i] - \
                                                        objectOfITEM_14127.OnHandFromPriorPeriod[i]
                objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT] = \
                    objectOfITEM_14127.NetRequirements[i]
                if objectOfITEM_14127.Q == 1:
                    objectOfITEM_14127.PlannedOrderRelases = objectOfITEM_14127.TimePhasedNetRequirements
                    objectOfITEM_14127.PlannedOrderDelivery = objectOfITEM_14127.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                        j += objectOfITEM_14127.Q
                        if j >= objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                            objectOfITEM_14127.PlannedOrderRelases[i - objectOfITEM_14127.LT] = j
                            objectOfITEM_14127.PlannedOrderDelivery[i] = objectOfITEM_14127.PlannedOrderRelases[
                                i - objectOfITEM_14127.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_14127.GrossRequirements[i] != 0 and objectOfITEM_14127.ScheduledReceipts[i] != 0 and \
                objectOfITEM_14127.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_14127.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_14127.GrossRequirements[i] - objectOfITEM_14127.ScheduledReceipts[i])
            if objectOfITEM_14127.OnHandFromPriorPeriod[i] > objectOfITEM_14127.GrossRequirements[i]:
                objectOfITEM_14127.NetRequirements[i] = 0
                objectOfITEM_14127.OnHandFromPriorPeriod[i + 1] = objectOfITEM_14127.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_14127.GrossRequirements[i]
                if objectOfITEM_14127.Q == 1:
                    objectOfITEM_14127.PlannedOrderRelases = objectOfITEM_14127.TimePhasedNetRequirements
                    objectOfITEM_14127.PlannedOrderDelivery = objectOfITEM_14127.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                        j += objectOfITEM_14127.Q
                        if j >= objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                            objectOfITEM_14127.PlannedOrderRelases[i - objectOfITEM_14127.LT] = j
                            objectOfITEM_14127.PlannedOrderDelivery[i] = objectOfITEM_14127.PlannedOrderRelases[
                                i - objectOfITEM_14127.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_14127.NetRequirements[i + 1] = objectOfITEM_14127.GrossRequirements[i + 1] - \
                                                            objectOfITEM_14127.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT] = \
                    objectOfITEM_14127.NetRequirements[i]
                if objectOfITEM_14127.Q == 1:
                    objectOfITEM_14127.PlannedOrderRelases = objectOfITEM_14127.TimePhasedNetRequirements
                    objectOfITEM_14127.PlannedOrderDelivery = objectOfITEM_14127.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                        j += objectOfITEM_14127.Q
                        if j >= objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                            objectOfITEM_14127.PlannedOrderRelases[i - objectOfITEM_14127.LT] = j
                            objectOfITEM_14127.PlannedOrderDelivery[i] = objectOfITEM_14127.PlannedOrderRelases[
                                i - objectOfITEM_14127.LT]
                            break
                        else:
                            continue


        elif objectOfITEM_14127.GrossRequirements[i] == 0 and objectOfITEM_14127.ScheduledReceipts[i] == 0 and \
                objectOfITEM_14127.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_14127.GrossRequirements[i] == 0 and objectOfITEM_14127.ScheduledReceipts[i] == 0 and \
                objectOfITEM_14127.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_14127.NetRequirements[i] = 0

        elif objectOfITEM_14127.GrossRequirements[i] != 0 and objectOfITEM_14127.ScheduledReceipts[i] == 0 and \
                objectOfITEM_14127.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_14127.NetRequirements[i] = objectOfITEM_14127.GrossRequirements[i] - \
                                                    objectOfITEM_14127.OnHandFromPriorPeriod[i]
            objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT] = \
                objectOfITEM_14127.NetRequirements[i]
            if objectOfITEM_14127.Q == 1:
                objectOfITEM_14127.PlannedOrderRelases = objectOfITEM_14127.TimePhasedNetRequirements
                objectOfITEM_14127.PlannedOrderDelivery = objectOfITEM_14127.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                    j += objectOfITEM_14127.Q
                    if j >= objectOfITEM_14127.TimePhasedNetRequirements[i - objectOfITEM_14127.LT]:
                        objectOfITEM_14127.PlannedOrderRelases[i - objectOfITEM_14127.LT] = j
                        objectOfITEM_14127.PlannedOrderDelivery[i] = objectOfITEM_14127.PlannedOrderRelases[
                            i - objectOfITEM_14127.LT]
                        break
                    else:
                        continue
        else:
            continue
    print('\n', "Gross Requirements: ", objectOfITEM_14127.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_14127.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_14127.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_14127.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_14127.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_14127.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_14127.PlannedOrderDelivery)


# 8 ITEM
def ITEM_2142():
    for i in range(len(objectOfITEM_2142.Period)):
        if objectOfITEM_2142.GrossRequirements[i] != 0 and objectOfITEM_2142.ScheduledReceipts[i] == 0 and \
                objectOfITEM_2142.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_2142.OnHandFromPriorPeriod[i] > objectOfITEM_2142.GrossRequirements[i]:
                objectOfITEM_2142.NetRequirements[i] = 0
                objectOfITEM_2142.OnHandFromPriorPeriod[i + 1] = objectOfITEM_2142.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_2142.GrossRequirements[i]
                if objectOfITEM_2142.Q == 1:
                    objectOfITEM_2142.PlannedOrderRelases = objectOfITEM_2142.TimePhasedNetRequirements
                    objectOfITEM_2142.PlannedOrderDelivery = objectOfITEM_2142.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                        j += objectOfITEM_2142.Q
                        if j >= objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                            objectOfITEM_2142.PlannedOrderRelases[i - objectOfITEM_2142.LT] = j
                            objectOfITEM_2142.PlannedOrderDelivery[i] = objectOfITEM_2142.PlannedOrderRelases[
                                i - objectOfITEM_2142.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_2142.NetRequirements[i] = objectOfITEM_2142.GrossRequirements[i] - \
                                                       objectOfITEM_2142.OnHandFromPriorPeriod[i]
                objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT] = \
                    objectOfITEM_2142.NetRequirements[i]
                if objectOfITEM_2142.Q == 1:
                    objectOfITEM_2142.PlannedOrderRelases = objectOfITEM_2142.TimePhasedNetRequirements
                    objectOfITEM_2142.PlannedOrderDelivery = objectOfITEM_2142.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                        j += objectOfITEM_2142.Q
                        if j >= objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                            objectOfITEM_2142.PlannedOrderRelases[i - objectOfITEM_2142.LT] = j
                            objectOfITEM_2142.PlannedOrderDelivery[i] = objectOfITEM_2142.PlannedOrderRelases[
                                i - objectOfITEM_2142.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_2142.GrossRequirements[i] != 0 and objectOfITEM_2142.ScheduledReceipts[i] != 0 and \
                objectOfITEM_2142.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_2142.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_2142.GrossRequirements[i] - objectOfITEM_2142.ScheduledReceipts[i])
            if objectOfITEM_2142.OnHandFromPriorPeriod[i] > objectOfITEM_2142.GrossRequirements[i]:
                objectOfITEM_2142.NetRequirements[i] = 0
                objectOfITEM_2142.OnHandFromPriorPeriod[i + 1] = objectOfITEM_2142.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_2142.GrossRequirements[i]
                if objectOfITEM_2142.Q == 1:
                    objectOfITEM_2142.PlannedOrderRelases = objectOfITEM_2142.TimePhasedNetRequirements
                    objectOfITEM_2142.PlannedOrderDelivery = objectOfITEM_2142.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                        j += objectOfITEM_2142.Q
                        if j >= objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                            objectOfITEM_2142.PlannedOrderRelases[i - objectOfITEM_2142.LT] = j
                            objectOfITEM_2142.PlannedOrderDelivery[i] = objectOfITEM_2142.PlannedOrderRelases[
                                i - objectOfITEM_2142.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_2142.NetRequirements[i + 1] = objectOfITEM_2142.GrossRequirements[i + 1] - \
                                                           objectOfITEM_2142.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT] = \
                    objectOfITEM_2142.NetRequirements[i]
                if objectOfITEM_2142.Q == 1:
                    objectOfITEM_2142.PlannedOrderRelases = objectOfITEM_2142.TimePhasedNetRequirements
                    objectOfITEM_2142.PlannedOrderDelivery = objectOfITEM_2142.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                        j += objectOfITEM_2142.Q
                        if j >= objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                            objectOfITEM_2142.PlannedOrderRelases[i - objectOfITEM_2142.LT] = j
                            objectOfITEM_2142.PlannedOrderDelivery[i] = objectOfITEM_2142.PlannedOrderRelases[
                                i - objectOfITEM_2142.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_2142.GrossRequirements[i] == 0 and objectOfITEM_2142.ScheduledReceipts[i] == 0 and \
                objectOfITEM_2142.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_2142.GrossRequirements[i] == 0 and objectOfITEM_2142.ScheduledReceipts[i] == 0 and \
                objectOfITEM_2142.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_2142.NetRequirements[i] = 0

        elif objectOfITEM_2142.GrossRequirements[i] != 0 and objectOfITEM_2142.ScheduledReceipts[i] == 0 and \
                objectOfITEM_2142.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_2142.NetRequirements[i] = objectOfITEM_2142.GrossRequirements[i] - \
                                                   objectOfITEM_2142.OnHandFromPriorPeriod[i]
            objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT] = objectOfITEM_2142.NetRequirements[i]
            if objectOfITEM_2142.Q == 1:
                objectOfITEM_2142.PlannedOrderRelases = objectOfITEM_2142.TimePhasedNetRequirements
                objectOfITEM_2142.PlannedOrderDelivery = objectOfITEM_2142.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                    j += objectOfITEM_2142.Q
                    if j >= objectOfITEM_2142.TimePhasedNetRequirements[i - objectOfITEM_2142.LT]:
                        objectOfITEM_2142.PlannedOrderRelases[i - objectOfITEM_2142.LT] = j
                        objectOfITEM_2142.PlannedOrderDelivery[i] = objectOfITEM_2142.PlannedOrderRelases[
                            i - objectOfITEM_2142.LT]
                        break
                    else:
                        continue

        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_2142.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_2142.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_2142.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_2142.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_2142.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_2142.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_2142.PlannedOrderDelivery)


# 9 ITEM
def ITEM_019():
    for i in range(len(objectOfITEM_019.Period)):
        if objectOfITEM_019.GrossRequirements[i] != 0 and objectOfITEM_019.ScheduledReceipts[i] == 0 and \
                objectOfITEM_019.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_019.OnHandFromPriorPeriod[i] > objectOfITEM_019.GrossRequirements[i]:
                objectOfITEM_019.NetRequirements[i] = 0
                objectOfITEM_019.OnHandFromPriorPeriod[i + 1] = objectOfITEM_019.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_019.GrossRequirements[i]
                if objectOfITEM_019.Q == 1:
                    objectOfITEM_019.PlannedOrderRelases = objectOfITEM_019.TimePhasedNetRequirements
                    objectOfITEM_019.PlannedOrderDelivery = objectOfITEM_019.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                        j += objectOfITEM_019.Q
                        if j >= objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                            objectOfITEM_019.PlannedOrderRelases[i - objectOfITEM_019.LT] = j
                            objectOfITEM_019.PlannedOrderDelivery[i] = objectOfITEM_019.PlannedOrderRelases[
                                i - objectOfITEM_019.LT]
                            break
                continue
            else:
                objectOfITEM_019.NetRequirements[i] = objectOfITEM_019.GrossRequirements[i] - \
                                                      objectOfITEM_019.OnHandFromPriorPeriod[i]
                objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT] = objectOfITEM_019.NetRequirements[
                    i]
                if objectOfITEM_019.Q == 1:
                    objectOfITEM_019.PlannedOrderRelases = objectOfITEM_019.TimePhasedNetRequirements
                    objectOfITEM_019.PlannedOrderDelivery = objectOfITEM_019.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                        j += objectOfITEM_019.Q
                        if j >= objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                            objectOfITEM_019.PlannedOrderRelases[i - objectOfITEM_019.LT] = j
                            objectOfITEM_019.PlannedOrderDelivery[i] = objectOfITEM_019.PlannedOrderRelases[
                                i - objectOfITEM_019.LT]
                            break
                continue
        elif objectOfITEM_019.GrossRequirements[i] != 0 and objectOfITEM_019.ScheduledReceipts[i] != 0 and \
                objectOfITEM_019.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_019.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_019.GrossRequirements[i] - objectOfITEM_019.ScheduledReceipts[i])
            if objectOfITEM_019.OnHandFromPriorPeriod[i] > objectOfITEM_019.GrossRequirements[i]:
                objectOfITEM_019.NetRequirements[i] = 0
                objectOfITEM_019.OnHandFromPriorPeriod[i + 1] = objectOfITEM_019.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_019.GrossRequirements[i]
                if objectOfITEM_019.Q == 1:
                    objectOfITEM_019.PlannedOrderRelases = objectOfITEM_019.TimePhasedNetRequirements
                    objectOfITEM_019.PlannedOrderDelivery = objectOfITEM_019.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                        j += objectOfITEM_019.Q
                        if j >= objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                            objectOfITEM_019.PlannedOrderRelases[i - objectOfITEM_019.LT] = j
                            objectOfITEM_019.PlannedOrderDelivery[i] = objectOfITEM_019.PlannedOrderRelases[
                                i - objectOfITEM_019.LT]
                            break
                continue

            else:
                objectOfITEM_019.NetRequirements[i + 1] = objectOfITEM_019.GrossRequirements[i + 1] - \
                                                          objectOfITEM_019.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT] = objectOfITEM_019.NetRequirements[
                    i]
                if objectOfITEM_019.Q == 1:
                    objectOfITEM_019.PlannedOrderRelases = objectOfITEM_019.TimePhasedNetRequirements
                    objectOfITEM_019.PlannedOrderDelivery = objectOfITEM_019.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                        j += objectOfITEM_019.Q
                        if j >= objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                            objectOfITEM_019.PlannedOrderRelases[i - objectOfITEM_019.LT] = j
                            objectOfITEM_019.PlannedOrderDelivery[i] = objectOfITEM_019.PlannedOrderRelases[
                                i - objectOfITEM_019.LT]
                            break
                continue

        elif objectOfITEM_019.GrossRequirements[i] == 0 and objectOfITEM_019.ScheduledReceipts[i] == 0 and \
                objectOfITEM_019.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_019.GrossRequirements[i] == 0 and objectOfITEM_019.ScheduledReceipts[i] == 0 and \
                objectOfITEM_019.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_019.NetRequirements[i] = 0

        elif objectOfITEM_019.GrossRequirements[i] != 0 and objectOfITEM_019.ScheduledReceipts[i] == 0 and \
                objectOfITEM_019.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_019.NetRequirements[i] = objectOfITEM_019.GrossRequirements[i] - \
                                                  objectOfITEM_019.OnHandFromPriorPeriod[i]
            objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT] = objectOfITEM_019.NetRequirements[i]
            if objectOfITEM_019.Q == 1:
                objectOfITEM_019.PlannedOrderRelases = objectOfITEM_019.TimePhasedNetRequirements
                objectOfITEM_019.PlannedOrderDelivery = objectOfITEM_019.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                    j += objectOfITEM_019.Q
                    if j >= objectOfITEM_019.TimePhasedNetRequirements[i - objectOfITEM_019.LT]:
                        objectOfITEM_019.PlannedOrderRelases[i - objectOfITEM_019.LT] = j
                        objectOfITEM_019.PlannedOrderDelivery[i] = objectOfITEM_019.PlannedOrderRelases[
                            i - objectOfITEM_019.LT]
                        break
            continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_019.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_019.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_019.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_019.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_019.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_019.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_019.PlannedOrderDelivery)


# 10 ITEM
def ITEM_457():
    for i in range(len(objectOfITEM_457.Period)):
        if objectOfITEM_457.GrossRequirements[i] != 0 and objectOfITEM_457.ScheduledReceipts[i] == 0 and \
                objectOfITEM_457.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_457.OnHandFromPriorPeriod[i] > objectOfITEM_457.GrossRequirements[i]:
                objectOfITEM_457.NetRequirements[i] = 0
                objectOfITEM_457.OnHandFromPriorPeriod[i + 1] = objectOfITEM_457.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_457.GrossRequirements[i]
                if objectOfITEM_457.Q == 1:
                    objectOfITEM_457.PlannedOrderRelases = objectOfITEM_457.TimePhasedNetRequirements
                    objectOfITEM_457.PlannedOrderDelivery = objectOfITEM_457.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                        j += objectOfITEM_457.Q
                        if j >= objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                            objectOfITEM_457.PlannedOrderRelases[i - objectOfITEM_457.LT] = j
                            objectOfITEM_457.PlannedOrderDelivery[i] = objectOfITEM_457.PlannedOrderRelases[
                                i - objectOfITEM_457.LT]
                            break
                continue
            else:
                objectOfITEM_457.NetRequirements[i] = objectOfITEM_457.GrossRequirements[i] - \
                                                      objectOfITEM_457.OnHandFromPriorPeriod[i]
                objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT] = objectOfITEM_457.NetRequirements[
                    i]
                if objectOfITEM_457.Q == 1:
                    objectOfITEM_457.PlannedOrderRelases = objectOfITEM_457.TimePhasedNetRequirements
                    objectOfITEM_457.PlannedOrderDelivery = objectOfITEM_457.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                        j += objectOfITEM_457.Q
                        if j >= objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                            objectOfITEM_457.PlannedOrderRelases[i - objectOfITEM_457.LT] = j
                            objectOfITEM_457.PlannedOrderDelivery[i] = objectOfITEM_457.PlannedOrderRelases[
                                i - objectOfITEM_457.LT]
                            break
                continue
        elif objectOfITEM_457.GrossRequirements[i] != 0 and objectOfITEM_457.ScheduledReceipts[i] != 0 and \
                objectOfITEM_457.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_457.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_457.GrossRequirements[i] - objectOfITEM_457.ScheduledReceipts[i])
            if objectOfITEM_457.OnHandFromPriorPeriod[i] > objectOfITEM_457.GrossRequirements[i]:
                objectOfITEM_457.NetRequirements[i] = 0
                objectOfITEM_457.OnHandFromPriorPeriod[i + 1] = objectOfITEM_457.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_457.GrossRequirements[i]
                if objectOfITEM_457.Q == 1:
                    objectOfITEM_457.PlannedOrderRelases = objectOfITEM_457.TimePhasedNetRequirements
                    objectOfITEM_457.PlannedOrderDelivery = objectOfITEM_457.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                        j += objectOfITEM_457.Q
                        if j >= objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                            objectOfITEM_457.PlannedOrderRelases[i - objectOfITEM_457.LT] = j
                            objectOfITEM_457.PlannedOrderDelivery[i] = objectOfITEM_457.PlannedOrderRelases[
                                i - objectOfITEM_457.LT]
                            break
                continue

            else:
                objectOfITEM_457.NetRequirements[i + 1] = objectOfITEM_457.GrossRequirements[i + 1] - \
                                                          objectOfITEM_457.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT] = objectOfITEM_457.NetRequirements[
                    i]
                if objectOfITEM_457.Q == 1:
                    objectOfITEM_457.PlannedOrderRelases = objectOfITEM_457.TimePhasedNetRequirements
                    objectOfITEM_457.PlannedOrderDelivery = objectOfITEM_457.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                        j += objectOfITEM_457.Q
                        if j >= objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                            objectOfITEM_457.PlannedOrderRelases[i - objectOfITEM_457.LT] = j
                            objectOfITEM_457.PlannedOrderDelivery[i] = objectOfITEM_457.PlannedOrderRelases[
                                i - objectOfITEM_457.LT]
                            break
                continue

        elif objectOfITEM_457.GrossRequirements[i] == 0 and objectOfITEM_457.ScheduledReceipts[i] == 0 and \
                objectOfITEM_457.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_457.GrossRequirements[i] == 0 and objectOfITEM_457.ScheduledReceipts[i] == 0 and \
                objectOfITEM_457.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_457.NetRequirements[i] = 0

        elif objectOfITEM_457.GrossRequirements[i] != 0 and objectOfITEM_457.ScheduledReceipts[i] == 0 and \
                objectOfITEM_457.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_457.NetRequirements[i] = objectOfITEM_457.GrossRequirements[i] - \
                                                  objectOfITEM_457.OnHandFromPriorPeriod[i]
            objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT] = objectOfITEM_457.NetRequirements[i]
            if objectOfITEM_457.Q == 1:
                objectOfITEM_457.PlannedOrderRelases = objectOfITEM_457.TimePhasedNetRequirements
                objectOfITEM_457.PlannedOrderDelivery = objectOfITEM_457.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                    j += objectOfITEM_457.Q
                    if j >= objectOfITEM_457.TimePhasedNetRequirements[i - objectOfITEM_457.LT]:
                        objectOfITEM_457.PlannedOrderRelases[i - objectOfITEM_457.LT] = j
                        objectOfITEM_457.PlannedOrderDelivery[i] = objectOfITEM_457.PlannedOrderRelases[
                            i - objectOfITEM_457.LT]
                        break
            continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_457.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_457.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_457.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_457.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_457.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_457.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_457.PlannedOrderDelivery)


# 11 ITEM
def ITEM_11495():
    for i in range(len(objectOfITEM_11495.Period)):
        if objectOfITEM_11495.GrossRequirements[i] != 0 and objectOfITEM_11495.ScheduledReceipts[i] == 0 and \
                objectOfITEM_11495.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_11495.OnHandFromPriorPeriod[i] > objectOfITEM_11495.GrossRequirements[i]:
                objectOfITEM_11495.NetRequirements[i] = 0
                objectOfITEM_11495.OnHandFromPriorPeriod[i + 1] = objectOfITEM_11495.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_11495.GrossRequirements[i]
                if objectOfITEM_11495.Q == 1:
                    objectOfITEM_11495.PlannedOrderRelases = objectOfITEM_11495.TimePhasedNetRequirements
                    objectOfITEM_11495.PlannedOrderDelivery = objectOfITEM_11495.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                        j += objectOfITEM_11495.Q
                        if j >= objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                            objectOfITEM_11495.PlannedOrderRelases[i - objectOfITEM_11495.LT] = j
                            objectOfITEM_11495.PlannedOrderDelivery[i] = objectOfITEM_11495.PlannedOrderRelases[
                                i - objectOfITEM_11495.LT]
                            break

            else:
                objectOfITEM_11495.NetRequirements[i] = objectOfITEM_11495.GrossRequirements[i] - \
                                                        objectOfITEM_11495.OnHandFromPriorPeriod[i]
                objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT] = \
                    objectOfITEM_11495.NetRequirements[i]
                if objectOfITEM_11495.Q == 1:
                    objectOfITEM_11495.PlannedOrderRelases = objectOfITEM_11495.TimePhasedNetRequirements
                    objectOfITEM_11495.PlannedOrderDelivery = objectOfITEM_11495.NetRequirements

                else:
                    j = 0
                    while j < objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                        j += objectOfITEM_11495.Q
                        if j >= objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                            objectOfITEM_11495.PlannedOrderRelases[i - objectOfITEM_11495.LT] = j
                            objectOfITEM_11495.PlannedOrderDelivery[i] = objectOfITEM_11495.PlannedOrderRelases[
                                i - objectOfITEM_11495.LT]
                            break

        elif objectOfITEM_11495.GrossRequirements[i] != 0 and objectOfITEM_11495.ScheduledReceipts[i] != 0 and \
                objectOfITEM_11495.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_11495.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_11495.GrossRequirements[i] - objectOfITEM_11495.ScheduledReceipts[i])
            if objectOfITEM_11495.OnHandFromPriorPeriod[i] > objectOfITEM_11495.GrossRequirements[i]:
                objectOfITEM_11495.NetRequirements[i] = 0
                objectOfITEM_11495.OnHandFromPriorPeriod[i + 1] = objectOfITEM_11495.OnHandFromPriorPeriod[i] - \
                                                                  objectOfITEM_11495.GrossRequirements[i]
                if objectOfITEM_11495.Q == 1:
                    objectOfITEM_11495.PlannedOrderRelases = objectOfITEM_11495.TimePhasedNetRequirements
                    objectOfITEM_11495.PlannedOrderDelivery = objectOfITEM_11495.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                        j += objectOfITEM_11495.Q
                        if j >= objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                            objectOfITEM_11495.PlannedOrderRelases[i - objectOfITEM_11495.LT] = j
                            objectOfITEM_11495.PlannedOrderDelivery[i] = objectOfITEM_11495.PlannedOrderRelases[
                                i - objectOfITEM_11495.LT]
                            break


            else:
                objectOfITEM_11495.NetRequirements[i + 1] = objectOfITEM_11495.GrossRequirements[i + 1] - \
                                                            objectOfITEM_11495.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT] = \
                    objectOfITEM_11495.NetRequirements[i]
                if objectOfITEM_11495.Q == 1:
                    objectOfITEM_11495.PlannedOrderRelases = objectOfITEM_11495.TimePhasedNetRequirements
                    objectOfITEM_11495.PlannedOrderDelivery = objectOfITEM_11495.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                        j += objectOfITEM_11495.Q
                        if j >= objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                            objectOfITEM_11495.PlannedOrderRelases[i - objectOfITEM_11495.LT] = j
                            objectOfITEM_11495.PlannedOrderDelivery[i] = objectOfITEM_11495.PlannedOrderRelases[
                                i - objectOfITEM_11495.LT]
                            break


        elif objectOfITEM_11495.GrossRequirements[i] == 0 and objectOfITEM_11495.ScheduledReceipts[i] == 0 and \
                objectOfITEM_11495.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_11495.GrossRequirements[i] == 0 and objectOfITEM_11495.ScheduledReceipts[i] == 0 and \
                objectOfITEM_11495.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_11495.NetRequirements[i] = 0

        elif objectOfITEM_11495.GrossRequirements[i] != 0 and objectOfITEM_11495.ScheduledReceipts[i] == 0 and \
                objectOfITEM_11495.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_11495.NetRequirements[i] = objectOfITEM_11495.GrossRequirements[i] - \
                                                    objectOfITEM_11495.OnHandFromPriorPeriod[i]
            objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT] = \
                objectOfITEM_11495.NetRequirements[i]
            if objectOfITEM_11495.Q == 1:
                objectOfITEM_11495.PlannedOrderRelases = objectOfITEM_11495.TimePhasedNetRequirements
                objectOfITEM_11495.PlannedOrderDelivery = objectOfITEM_11495.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                    j += objectOfITEM_11495.Q
                    if j >= objectOfITEM_11495.TimePhasedNetRequirements[i - objectOfITEM_11495.LT]:
                        objectOfITEM_11495.PlannedOrderRelases[i - objectOfITEM_11495.LT] = j
                        objectOfITEM_11495.PlannedOrderDelivery[i] = objectOfITEM_11495.PlannedOrderRelases[
                            i - objectOfITEM_11495.LT]
                        break
            continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_11495.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_11495.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_11495.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_11495.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_11495.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_11495.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_11495.PlannedOrderDelivery)
    objectOfITEM_129.GrossRequirements = objectOfITEM_11495.PlannedOrderRelases
    objectOfITEM_1118.GrossRequirements = objectOfITEM_11495.PlannedOrderRelases


# 12 ITEM
def ITEM_129():
    for i in range(len(objectOfITEM_129.Period)):
        if objectOfITEM_129.GrossRequirements[i] != 0 and objectOfITEM_129.ScheduledReceipts[i] == 0 and \
                objectOfITEM_129.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_129.OnHandFromPriorPeriod[i] > objectOfITEM_129.GrossRequirements[i]:
                objectOfITEM_129.NetRequirements[i] = 0
                objectOfITEM_129.OnHandFromPriorPeriod[i + 1] = objectOfITEM_129.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_129.GrossRequirements[i]
                if objectOfITEM_129.Q == 1:
                    objectOfITEM_129.PlannedOrderRelases = objectOfITEM_129.TimePhasedNetRequirements
                    objectOfITEM_129.PlannedOrderDelivery = objectOfITEM_129.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                        j += objectOfITEM_129.Q
                        if j >= objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                            objectOfITEM_129.PlannedOrderRelases[i - objectOfITEM_129.LT] = j
                            objectOfITEM_129.PlannedOrderDelivery[i] = objectOfITEM_129.PlannedOrderRelases[
                                i - objectOfITEM_129.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_129.NetRequirements[i] = objectOfITEM_129.GrossRequirements[i] - \
                                                      objectOfITEM_129.OnHandFromPriorPeriod[i]
                objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT] = objectOfITEM_129.NetRequirements[
                    i]
                if objectOfITEM_129.Q == 1:
                    objectOfITEM_129.PlannedOrderRelases = objectOfITEM_129.TimePhasedNetRequirements
                    objectOfITEM_129.PlannedOrderDelivery = objectOfITEM_129.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                        j += objectOfITEM_129.Q
                        if j >= objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                            objectOfITEM_129.PlannedOrderRelases[i - objectOfITEM_129.LT] = j
                            objectOfITEM_129.PlannedOrderDelivery[i] = objectOfITEM_129.PlannedOrderRelases[
                                i - objectOfITEM_129.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_129.GrossRequirements[i] != 0 and objectOfITEM_129.ScheduledReceipts[i] != 0 and \
                objectOfITEM_129.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_129.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_129.GrossRequirements[i] - objectOfITEM_129.ScheduledReceipts[i])
            if objectOfITEM_129.OnHandFromPriorPeriod[i] > objectOfITEM_129.GrossRequirements[i]:
                objectOfITEM_129.NetRequirements[i] = 0
                objectOfITEM_129.OnHandFromPriorPeriod[i + 1] = objectOfITEM_129.OnHandFromPriorPeriod[i] - \
                                                                objectOfITEM_129.GrossRequirements[i]
                if objectOfITEM_129.Q == 1:
                    objectOfITEM_129.PlannedOrderRelases = objectOfITEM_129.TimePhasedNetRequirements
                    objectOfITEM_129.PlannedOrderDelivery = objectOfITEM_129.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                        j += objectOfITEM_129.Q
                        if j >= objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                            objectOfITEM_129.PlannedOrderRelases[i - objectOfITEM_129.LT] = j
                            objectOfITEM_129.PlannedOrderDelivery[i] = objectOfITEM_129.PlannedOrderRelases[
                                i - objectOfITEM_129.LT]
                            break
                        else:
                            continue


            else:
                objectOfITEM_129.NetRequirements[i + 1] = objectOfITEM_129.GrossRequirements[i + 1] - \
                                                          objectOfITEM_129.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT] = objectOfITEM_129.NetRequirements[
                    i]
                if objectOfITEM_129.Q == 1:
                    objectOfITEM_129.PlannedOrderRelases = objectOfITEM_129.TimePhasedNetRequirements
                    objectOfITEM_129.PlannedOrderDelivery = objectOfITEM_129.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                        j += objectOfITEM_129.Q
                        if j >= objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                            objectOfITEM_129.PlannedOrderRelases[i - objectOfITEM_129.LT] = j
                            objectOfITEM_129.PlannedOrderDelivery[i] = objectOfITEM_129.PlannedOrderRelases[
                                i - objectOfITEM_129.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_129.GrossRequirements[i] == 0 and objectOfITEM_129.ScheduledReceipts[i] == 0 and \
                objectOfITEM_129.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_129.GrossRequirements[i] == 0 and objectOfITEM_129.ScheduledReceipts[i] == 0 and \
                objectOfITEM_129.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_129.NetRequirements[i] = 0

        elif objectOfITEM_129.GrossRequirements[i] != 0 and objectOfITEM_129.ScheduledReceipts[i] == 0 and \
                objectOfITEM_129.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_129.NetRequirements[i] = objectOfITEM_129.GrossRequirements[i] - \
                                                  objectOfITEM_129.OnHandFromPriorPeriod[i]
            objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT] = objectOfITEM_129.NetRequirements[i]
            if objectOfITEM_129.Q == 1:
                objectOfITEM_129.PlannedOrderRelases = objectOfITEM_129.TimePhasedNetRequirements
                objectOfITEM_129.PlannedOrderDelivery = objectOfITEM_129.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                    j += objectOfITEM_129.Q
                    if j >= objectOfITEM_129.TimePhasedNetRequirements[i - objectOfITEM_129.LT]:
                        objectOfITEM_129.PlannedOrderRelases[i - objectOfITEM_129.LT] = j
                        objectOfITEM_129.PlannedOrderDelivery[i] = objectOfITEM_129.PlannedOrderRelases[
                            i - objectOfITEM_129.LT]
                        break
                    else:
                        continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_129.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_129.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_129.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_129.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_129.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_129.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_129.PlannedOrderDelivery)


# 13 ITEM
def ITEM_1118():
    for i in range(len(objectOfITEM_1118.Period)):
        if objectOfITEM_1118.GrossRequirements[i] != 0 and objectOfITEM_1118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1118.OnHandFromPriorPeriod[i] != 0:
            if objectOfITEM_1118.OnHandFromPriorPeriod[i] > objectOfITEM_1118.GrossRequirements[i]:
                objectOfITEM_1118.NetRequirements[i] = 0
                objectOfITEM_1118.OnHandFromPriorPeriod[i + 1] = objectOfITEM_1118.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_1118.GrossRequirements[i]
                if objectOfITEM_1118.Q == 1:
                    objectOfITEM_1118.PlannedOrderRelases = objectOfITEM_1118.TimePhasedNetRequirements
                    objectOfITEM_1118.PlannedOrderDelivery = objectOfITEM_1118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                        j += objectOfITEM_1118.Q
                        if j >= objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                            objectOfITEM_1118.PlannedOrderRelases[i - objectOfITEM_1118.LT] = j
                            objectOfITEM_1118.PlannedOrderDelivery[i] = objectOfITEM_1118.PlannedOrderRelases[
                                i - objectOfITEM_1118.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_1118.NetRequirements[i] = objectOfITEM_1118.GrossRequirements[i] - \
                                                       objectOfITEM_1118.OnHandFromPriorPeriod[i]
                objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT] = \
                    objectOfITEM_1118.NetRequirements[i]
                if objectOfITEM_1118.Q == 1:
                    objectOfITEM_1118.PlannedOrderRelases = objectOfITEM_1118.TimePhasedNetRequirements
                    objectOfITEM_1118.PlannedOrderDelivery = objectOfITEM_1118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                        j += objectOfITEM_1118.Q
                        if j >= objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                            objectOfITEM_1118.PlannedOrderRelases[i - objectOfITEM_1118.LT] = j
                            objectOfITEM_1118.PlannedOrderDelivery[i] = objectOfITEM_1118.PlannedOrderRelases[
                                i - objectOfITEM_1118.LT]
                            break
                        else:
                            continue
        elif objectOfITEM_1118.GrossRequirements[i] != 0 and objectOfITEM_1118.ScheduledReceipts[i] != 0 and \
                objectOfITEM_1118.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_1118.OnHandFromPriorPeriod[i + 1] = abs(
                objectOfITEM_1118.GrossRequirements[i] - objectOfITEM_1118.ScheduledReceipts[i])
            if objectOfITEM_1118.OnHandFromPriorPeriod[i] > objectOfITEM_1118.GrossRequirements[i]:
                objectOfITEM_1118.NetRequirements[i] = 0
                objectOfITEM_1118.OnHandFromPriorPeriod[i + 1] = objectOfITEM_1118.OnHandFromPriorPeriod[i] - \
                                                                 objectOfITEM_1118.GrossRequirements[i]
                if objectOfITEM_1118.Q == 1:
                    objectOfITEM_1118.PlannedOrderRelases = objectOfITEM_1118.TimePhasedNetRequirements
                    objectOfITEM_1118.PlannedOrderDelivery = objectOfITEM_1118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                        j += objectOfITEM_1118.Q
                        if j >= objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                            objectOfITEM_1118.PlannedOrderRelases[i - objectOfITEM_1118.LT] = j
                            objectOfITEM_1118.PlannedOrderDelivery[i] = objectOfITEM_1118.PlannedOrderRelases[
                                i - objectOfITEM_1118.LT]
                            break
                        else:
                            continue

            else:
                objectOfITEM_1118.NetRequirements[i + 1] = objectOfITEM_1118.GrossRequirements[i + 1] - \
                                                           objectOfITEM_1118.OnHandFromPriorPeriod[i + 1]

                objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT] = \
                    objectOfITEM_1118.NetRequirements[i]
                if objectOfITEM_1118.Q == 1:
                    objectOfITEM_1118.PlannedOrderRelases = objectOfITEM_1118.TimePhasedNetRequirements
                    objectOfITEM_1118.PlannedOrderDelivery = objectOfITEM_1118.NetRequirements
                else:
                    j = 0
                    while j < objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                        j += objectOfITEM_1118.Q
                        if j >= objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                            objectOfITEM_1118.PlannedOrderRelases[i - objectOfITEM_1118.LT] = j
                            objectOfITEM_1118.PlannedOrderDelivery[i] = objectOfITEM_1118.PlannedOrderRelases[
                                i - objectOfITEM_1118.LT]
                            break
                        else:
                            continue

        elif objectOfITEM_1118.GrossRequirements[i] == 0 and objectOfITEM_1118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1118.OnHandFromPriorPeriod[i] == 0:
            continue
        elif objectOfITEM_1118.GrossRequirements[i] == 0 and objectOfITEM_1118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1118.OnHandFromPriorPeriod[i] != 0:

            objectOfITEM_1118.NetRequirements[i] = 0

        elif objectOfITEM_1118.GrossRequirements[i] != 0 and objectOfITEM_1118.ScheduledReceipts[i] == 0 and \
                objectOfITEM_1118.OnHandFromPriorPeriod[i] == 0:
            objectOfITEM_1118.NetRequirements[i] = objectOfITEM_1118.GrossRequirements[i] - \
                                                   objectOfITEM_1118.OnHandFromPriorPeriod[i]
            objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT] = objectOfITEM_1118.NetRequirements[i]
            if objectOfITEM_1118.Q == 1:
                objectOfITEM_1118.PlannedOrderRelases = objectOfITEM_1118.TimePhasedNetRequirements
                objectOfITEM_1118.PlannedOrderDelivery = objectOfITEM_1118.NetRequirements
            else:
                j = 0
                while j < objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                    j += objectOfITEM_1118.Q
                    if j >= objectOfITEM_1118.TimePhasedNetRequirements[i - objectOfITEM_1118.LT]:
                        objectOfITEM_1118.PlannedOrderRelases[i - objectOfITEM_1118.LT] = j
                        objectOfITEM_1118.PlannedOrderDelivery[i] = objectOfITEM_1118.PlannedOrderRelases[
                            i - objectOfITEM_1118.LT]
                        break
                    else:
                        continue
        else:
            continue

    print('\n', "Gross Requirements: ", objectOfITEM_1118.GrossRequirements, '\n', "Scheduled Receipts: ",
          objectOfITEM_1118.ScheduledReceipts, '\n',
          "On Hand From Prior Period: ", objectOfITEM_1118.OnHandFromPriorPeriod, '\n',
          "NetRequirements: ", objectOfITEM_1118.NetRequirements, '\n', "Time Phased Net Requirements",
          objectOfITEM_1118.TimePhasedNetRequirements, '\n',
          "Planned Order Relases: ", objectOfITEM_1118.PlannedOrderRelases, '\n', "Planned Order Delivery: ",
          objectOfITEM_1118.PlannedOrderDelivery)


def PRINT():
    print('\n', "ITEM", objectOfITEM_1605.ID, "Shovel complete")
    ITEM_1605()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_13122.ID, "Top handle")
    ITEM_13122()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_048.ID, "Scoop-shaft")
    ITEM_048()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_118.ID, "Shaft")
    ITEM_118()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_314.ID, "assembly")
    ITEM_314()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_062.ID, "Nail")
    ITEM_062()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_14127.ID, "Rivet")
    ITEM_14127()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_2142.ID, "Scoop")
    ITEM_2142()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_019.ID, "Blade")
    ITEM_019()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_457.ID, "Top handle")
    ITEM_457()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_11495.ID, "Bracelet")
    ITEM_11495()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_129.ID, "Top handle")
    ITEM_129()
    print("--------------------------------------------------------------------------")
    print('\n', "ITEM", objectOfITEM_1118.ID, "Top handle")
    ITEM_1118()


PRINT()
