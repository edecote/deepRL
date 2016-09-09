import environment.gridWorld as gw
import learner.DQN as q

def main(argv=None):
    q.train()
    q.testAlgo()
    # state = gw.initGrid()
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # state = gw.makeMove(state, 3)
    # print('Reward: %s' % (gw.getReward(state),))
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # state = gw.makeMove(state, 3)
    # print('Reward: %s' % (gw.getReward(state),))
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # state = gw.makeMove(state, 1)
    # print('Reward: %s' % (gw.getReward(state),))
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # state = gw.makeMove(state, 1)
    # print('Reward: %s' % (gw.getReward(state),))
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # state = gw.makeMove(state, 1)
    # print('Reward: %s' % (gw.getReward(state),))
    # print(gw.dispGrid(state))
    # print(q.model.predict(state.reshape(1, 64), batch_size=1))
    # just to show an example output; read outputs left to right: up/down/left/right

if __name__ == '__main__':
    main()