from pprint import pprint
import argparse

def parse_args():

    parser = argparse.ArgumentParser()
    # Data input settings
    parser.add_argument('--dataset', type=str, default='refcocog', help='name of dataset')
    # Optimization: General
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--epochs', type=int,help='Number of epochs',default=50)
    parser.add_argument('--workers', type=int,help='Number of workers',default=2)
    parser.add_argument('--model', help='Model Q | I| QI | Main | RN',default='boxonly')
    parser.add_argument('--evalsplit', help='eval spolit',default='val')
    parser.add_argument('--lr', type=float,default=0.0003,help='Learning rate')
    parser.add_argument('--save', help='save folder name',default='0try')
    parser.add_argument('--seed', type=int, default=1111, help='random seed')
    parser.add_argument('--load', type=str, default=None, help='load chkpoint file name')
    parser.add_argument('--resume',  action='store_true', help='resume train from load chkpoint')
    parser.add_argument('--test', action='store_true', help='test only')
    parser.add_argument('--savejson',action='store_true',help='save json in VQA format')
    parser.add_argument('--savemodel',action='store_true',help='checkpoint save the model')
    parser.add_argument('--testrun', action='store_true', help='test run with few dataset')
    parser.add_argument('--expl', type=str, default='info', help='extra explanation of the method')
   
    # parse 
    args = parser.parse_args()
    opt = vars(args)
    pprint('parsed input parameters:')
    pprint(opt)
    return args

if __name__ == '__main__':

    opt = parse_args()
    print('opt[\'dataset\'] is ', opt.dataset)




