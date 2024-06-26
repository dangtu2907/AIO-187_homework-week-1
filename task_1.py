def evaluate_classification_model(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1-Score: {f1_score:.2f}')

try:
    tp = int(input('Nhập tp: '))
    fp = int(input('Nhập fp: '))
    fn = int(input('Nhập fn: '))
        
except ValueError as e:
    print(e)
    print('All inputs must be integers')
if  tp <= 0 or fp <= 0 or fn <= 0:
    print("tp, fp and fn must be greater than 0")
else:
    evaluate_classification_model(tp, fp, fn) 
