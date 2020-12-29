//idea: maintain double linked-list for O(1) insHead-delAny-movetohead-gettail
//also maintain a map/dict for O(1) access.
//put: check map for exists:yes->update, no->insHead, check capacity and evict tail
//get: check map for exists:yes->moveToHead+return val, no->return -1
class LRUCache {
public:
    class dlinklist{
        public:
        dlinklist(int k, int v){
            this->key=k;
            this->value=v;
            
        }
        int key;
        int value;
        dlinklist* prev;
        dlinklist* next;
    };
    int capacity;
    dlinklist* head;
    dlinklist* tail;
    unordered_map<int, dlinklist*> sp;
    
    void additem(dlinklist* item){
        //insert at head <item> head->next
        dlinklist* tmp = this->head->next;
        
        this->head->next = item;
        item->prev=this->head;
        item->next=tmp;
        tmp->prev=item;
        
    }
    void removeitem(dlinklist* item){
        item->prev->next = item->next;
        item->next->prev = item->prev;
    }
    void moveToHead(dlinklist* item){        
        //remove without free
        this->removeitem(item);
        //insert to head
        this->additem(item);
    }
    
    LRUCache(int capacity) {
        this->capacity=capacity;
        this->head= new dlinklist(0,0);
        this->tail= new dlinklist(-1,-1);
        this->head->prev=NULL;
        this->head->next=this->tail;//head->tail
        this->tail->prev=this->head;//head<-tail
        
    }
    ~LRUCache(){
        
    }
    
    int get(int key) {
        //cout<<"get "<<"k="<<key<<endl;
        auto it = this->sp.find(key);
        if(it!=sp.end()){
            moveToHead(it->second);//LRU move it to head
            return it->second->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        //normal put
        //cout<<"put "<<"k="<<key<<",v="<<value<<endl;
        dlinklist* item = NULL;
        auto it = this->sp.find(key);
        if(it!=sp.end()){
            //update
            //cout<<"found exist,update"<<it->second<<endl;
            item=it->second;
            moveToHead(item);
            item->value=value;
        }
        else{
            //create
            item=new dlinklist(key,value);
            this->additem(item);
        }
        sp[key]=item;
        
        //deal with lru
        if(sp.size()>capacity){
            dlinklist* eldest = this->tail->prev;
            
            sp.erase(eldest->key);
            this->removeitem(eldest);
            //cout<<"item "<<eldest->key<<","<<eldest->value<<"freed"<<endl;
            delete eldest;//free it
            
        }
        
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */