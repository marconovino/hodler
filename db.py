from asyncpg import create_pool
from os import getenv

coinlist = ['1INCH', 'AAVE', 'ACM', 'ADA', 'AERGO', 'ALGO', 'ALICE', 'ALPHA', 'ANT', 'AR', 'ATOM', 'AUCTION', 'AUD', 'AUDIO', 'AUTO', 'AVA', 'AVAX', 'AXS', 'BADGER', 'BAKE', 'BAL', 'BAND', 'BAR', 'BAT', 'BCHA', 'BCH', 'BEL', 'BIFI', 'BNB', 'BNT', 'BTC', 'BTCST', 'BTG', 'BTT', 'BURGER', 'BZRX', 'CAKE', 'CFX', 'CHZ', 'CKB', 'COMP', 'COVER', 'CREAM', 'CRV', 'CTK', 'CTSI', 'CVP', 'DASH', 'DATA', 'DEGO', 'DEXE', 'DF', 'DGB', 'DIA', 'DNT', 'DODO', 'DOGE', 'DOT', 'EGLD', 'ENJ', 'EOS', 'EPS', 'ETC', 'ETH', 'EUR', 'FIL', 'FIO', 'FIS', 'FLM', 'FOR', 'FORTH', 'FRONT', 'FXS', 'GBP', 'GHST', 'GRT', 'HARD', 'HBAR', 'HEGIC', 'HOT', 'ICP', 'ICX', 'IDEX', 'INJ', 'IOST', 'IOTA', 'IQ', 'JST', 'JUV', 'KNC', 'KP3R', 'KSM', 'LINA', 'LINK', 'LIT', 'LRC', 'LTC', '', 'LUNA', 'MANA', 'MATIC', 'MIR', 'MKR', 'NANO', 'NEAR', 'NEO', 'NMR', 'OCEAN', 'OM', 'OMG', 'ONE', 'ONT', 'PAX', 'PERP', 'PHA', 'POLS', 'POND', 'PROM', 'PSG', 'QTUM', 'RAMP', 'REEF', 'ROSE', 'RSR', 'RUNE', 'RVN', 'SAND', 'SFP', 'SHIB', 'SKL', 'SLP', 'SNX', 'SOL', 'SRM', 'STRAX', 'SUPER', 'SUSHI', 'SWRV', 'SXP', 'SYS', 'TKO', 'TLM', 'TOMO', 'TRB', 'TRU', 'TRX', 'TUSD', 'TVK', 'TWT', 'UFT', 'UNFI', 'UNI', 'USDC', 'VET', 'VIDT', 'WAVES', 'WING', 'WRX', 'XLM', 'XMR', 'XRP', 'XTZ', 'XVG', 'XVS', 'YFI', 'YFII', 'ZEC', 'ZIL', 'ZRX']

CREATE = """CREATE TABLE IF NOT EXISTS Users (
  id BIGINT NOT NULL PRIMARY KEY,
  balance BIGINT NOT NULL DEFAULT 0,
  1INCHamnt BIGINT NOT NULL DEFAULT 0,    
  AAVEamnt BIGINT NOT NULL DEFAULT 0,   
  ACMamnt BIGINT NOT NULL DEFAULT 0,    
  ADAamnt BIGINT NOT NULL DEFAULT 0,    
  AERGOamnt BIGINT NOT NULL DEFAULT 0,  
  ALGOamnt BIGINT NOT NULL DEFAULT 0,   
  ALICEamnt BIGINT NOT NULL DEFAULT 0,  
  ALPHAamnt BIGINT NOT NULL DEFAULT 0,  
  ANTamnt BIGINT NOT NULL DEFAULT 0,    
  ARamnt BIGINT NOT NULL DEFAULT 0,     
  ATOMamnt BIGINT NOT NULL DEFAULT 0,   
  AUCTIONamnt BIGINT NOT NULL DEFAULT 0,
  AUDamnt BIGINT NOT NULL DEFAULT 0,
  AUDIOamnt BIGINT NOT NULL DEFAULT 0,
  AUTOamnt BIGINT NOT NULL DEFAULT 0,
  AVAamnt BIGINT NOT NULL DEFAULT 0,
  AVAXamnt BIGINT NOT NULL DEFAULT 0,
  AXSamnt BIGINT NOT NULL DEFAULT 0,
  BADGERamnt BIGINT NOT NULL DEFAULT 0,
  BAKEamnt BIGINT NOT NULL DEFAULT 0,
  BALamnt BIGINT NOT NULL DEFAULT 0,
  BANDamnt BIGINT NOT NULL DEFAULT 0,
  BARamnt BIGINT NOT NULL DEFAULT 0,
  BATamnt BIGINT NOT NULL DEFAULT 0,
  BCHAamnt BIGINT NOT NULL DEFAULT 0,
  BCHamnt BIGINT NOT NULL DEFAULT 0,
  BELamnt BIGINT NOT NULL DEFAULT 0,
  BIFIamnt BIGINT NOT NULL DEFAULT 0,
  BNBamnt BIGINT NOT NULL DEFAULT 0,
  BNTamnt BIGINT NOT NULL DEFAULT 0,
  BTCamnt BIGINT NOT NULL DEFAULT 0,
  BTCSTamnt BIGINT NOT NULL DEFAULT 0,
  BTGamnt BIGINT NOT NULL DEFAULT 0,
  BTTamnt BIGINT NOT NULL DEFAULT 0,
  BURGERamnt BIGINT NOT NULL DEFAULT 0,
  BZRXamnt BIGINT NOT NULL DEFAULT 0,
  CAKEamnt BIGINT NOT NULL DEFAULT 0,
  CFXamnt BIGINT NOT NULL DEFAULT 0,
  CHZamnt BIGINT NOT NULL DEFAULT 0,
  CKBamnt BIGINT NOT NULL DEFAULT 0,
  COMPamnt BIGINT NOT NULL DEFAULT 0,
  COVERamnt BIGINT NOT NULL DEFAULT 0,
  CREAMamnt BIGINT NOT NULL DEFAULT 0,
  CRVamnt BIGINT NOT NULL DEFAULT 0,
  CTKamnt BIGINT NOT NULL DEFAULT 0,
  CTSIamnt BIGINT NOT NULL DEFAULT 0,
  CVPamnt BIGINT NOT NULL DEFAULT 0,
  DASHamnt BIGINT NOT NULL DEFAULT 0,
  DATAamnt BIGINT NOT NULL DEFAULT 0,
  DEGOamnt BIGINT NOT NULL DEFAULT 0,
  DEXEamnt BIGINT NOT NULL DEFAULT 0,
  DFamnt BIGINT NOT NULL DEFAULT 0,
  DGBamnt BIGINT NOT NULL DEFAULT 0,
  DIAamnt BIGINT NOT NULL DEFAULT 0,
  DNTamnt BIGINT NOT NULL DEFAULT 0,
  DODOamnt BIGINT NOT NULL DEFAULT 0,
  DOGEamnt BIGINT NOT NULL DEFAULT 0,
  DOTamnt BIGINT NOT NULL DEFAULT 0,
  EGLDamnt BIGINT NOT NULL DEFAULT 0,
  ENJamnt BIGINT NOT NULL DEFAULT 0,
  EOSamnt BIGINT NOT NULL DEFAULT 0,
  EPSamnt BIGINT NOT NULL DEFAULT 0,
  ETCamnt BIGINT NOT NULL DEFAULT 0,
  ETHamnt BIGINT NOT NULL DEFAULT 0,
  EURamnt BIGINT NOT NULL DEFAULT 0,
  FILamnt BIGINT NOT NULL DEFAULT 0,
  FIOamnt BIGINT NOT NULL DEFAULT 0,
  FISamnt BIGINT NOT NULL DEFAULT 0,
  FLMamnt BIGINT NOT NULL DEFAULT 0,
  FORamnt BIGINT NOT NULL DEFAULT 0,
  FORTHamnt BIGINT NOT NULL DEFAULT 0,
  FRONTamnt BIGINT NOT NULL DEFAULT 0,
  FXSamnt BIGINT NOT NULL DEFAULT 0,
  GBPamnt BIGINT NOT NULL DEFAULT 0,
  GHSTamnt BIGINT NOT NULL DEFAULT 0,
  GRTamnt BIGINT NOT NULL DEFAULT 0,
  HARDamnt BIGINT NOT NULL DEFAULT 0,
  HBARamnt BIGINT NOT NULL DEFAULT 0,
  HEGICamnt BIGINT NOT NULL DEFAULT 0,
  HOTamnt BIGINT NOT NULL DEFAULT 0,
  ICPamnt BIGINT NOT NULL DEFAULT 0,
  ICXamnt BIGINT NOT NULL DEFAULT 0,
  IDEXamnt BIGINT NOT NULL DEFAULT 0,
  INJamnt BIGINT NOT NULL DEFAULT 0,
  IOSTamnt BIGINT NOT NULL DEFAULT 0,
  IOTAamnt BIGINT NOT NULL DEFAULT 0,
  IQamnt BIGINT NOT NULL DEFAULT 0,
  JSTamnt BIGINT NOT NULL DEFAULT 0,
  JUVamnt BIGINT NOT NULL DEFAULT 0,
  KNCamnt BIGINT NOT NULL DEFAULT 0,
  KP3Ramnt BIGINT NOT NULL DEFAULT 0,
  KSMamnt BIGINT NOT NULL DEFAULT 0,
  LINAamnt BIGINT NOT NULL DEFAULT 0,
  LINKamnt BIGINT NOT NULL DEFAULT 0,
  LITamnt BIGINT NOT NULL DEFAULT 0,
  LRCamnt BIGINT NOT NULL DEFAULT 0,
  LTCamnt BIGINT NOT NULL DEFAULT 0,
  amnt BIGINT NOT NULL DEFAULT 0,
  LUNAamnt BIGINT NOT NULL DEFAULT 0,
  MANAamnt BIGINT NOT NULL DEFAULT 0,
  MATICamnt BIGINT NOT NULL DEFAULT 0,
  MIRamnt BIGINT NOT NULL DEFAULT 0,
  MKRamnt BIGINT NOT NULL DEFAULT 0,
  NANOamnt BIGINT NOT NULL DEFAULT 0,
  NEARamnt BIGINT NOT NULL DEFAULT 0,
  NEOamnt BIGINT NOT NULL DEFAULT 0,
  NMRamnt BIGINT NOT NULL DEFAULT 0,
  OCEANamnt BIGINT NOT NULL DEFAULT 0,
  OMamnt BIGINT NOT NULL DEFAULT 0,
  OMGamnt BIGINT NOT NULL DEFAULT 0,
  ONEamnt BIGINT NOT NULL DEFAULT 0,
  ONTamnt BIGINT NOT NULL DEFAULT 0,
  PAXamnt BIGINT NOT NULL DEFAULT 0,
  PERPamnt BIGINT NOT NULL DEFAULT 0,
  PHAamnt BIGINT NOT NULL DEFAULT 0,
  POLSamnt BIGINT NOT NULL DEFAULT 0,
  PONDamnt BIGINT NOT NULL DEFAULT 0,
  PROMamnt BIGINT NOT NULL DEFAULT 0,
  PSGamnt BIGINT NOT NULL DEFAULT 0,
  QTUMamnt BIGINT NOT NULL DEFAULT 0,
  RAMPamnt BIGINT NOT NULL DEFAULT 0,
  REEFamnt BIGINT NOT NULL DEFAULT 0,
  ROSEamnt BIGINT NOT NULL DEFAULT 0,
  RSRamnt BIGINT NOT NULL DEFAULT 0,
  RUNEamnt BIGINT NOT NULL DEFAULT 0,
  RVNamnt BIGINT NOT NULL DEFAULT 0,
  SANDamnt BIGINT NOT NULL DEFAULT 0,
  SFPamnt BIGINT NOT NULL DEFAULT 0,
  SHIBamnt BIGINT NOT NULL DEFAULT 0,
  SKLamnt BIGINT NOT NULL DEFAULT 0,
  SLPamnt BIGINT NOT NULL DEFAULT 0,
  SNXamnt BIGINT NOT NULL DEFAULT 0,
  SOLamnt BIGINT NOT NULL DEFAULT 0,
  SRMamnt BIGINT NOT NULL DEFAULT 0,
  STRAXamnt BIGINT NOT NULL DEFAULT 0,
  SUPERamnt BIGINT NOT NULL DEFAULT 0,
  SUSHIamnt BIGINT NOT NULL DEFAULT 0,
  SWRVamnt BIGINT NOT NULL DEFAULT 0,
  SXPamnt BIGINT NOT NULL DEFAULT 0,
  SYSamnt BIGINT NOT NULL DEFAULT 0,
  TKOamnt BIGINT NOT NULL DEFAULT 0,
  TLMamnt BIGINT NOT NULL DEFAULT 0,
  TOMOamnt BIGINT NOT NULL DEFAULT 0,
  TRBamnt BIGINT NOT NULL DEFAULT 0,
  TRUamnt BIGINT NOT NULL DEFAULT 0,
  TRXamnt BIGINT NOT NULL DEFAULT 0,
  TUSDamnt BIGINT NOT NULL DEFAULT 0,
  TVKamnt BIGINT NOT NULL DEFAULT 0,
  TWTamnt BIGINT NOT NULL DEFAULT 0,
  UFTamnt BIGINT NOT NULL DEFAULT 0,
  UNFIamnt BIGINT NOT NULL DEFAULT 0,
  UNIamnt BIGINT NOT NULL DEFAULT 0,
  USDCamnt BIGINT NOT NULL DEFAULT 0,
  VETamnt BIGINT NOT NULL DEFAULT 0,
  VIDTamnt BIGINT NOT NULL DEFAULT 0,
  WAVESamnt BIGINT NOT NULL DEFAULT 0,
  WINGamnt BIGINT NOT NULL DEFAULT 0,
  WRXamnt BIGINT NOT NULL DEFAULT 0,
  XLMamnt BIGINT NOT NULL DEFAULT 0,
  XMRamnt BIGINT NOT NULL DEFAULT 0,
  XRPamnt BIGINT NOT NULL DEFAULT 0,
  XTZamnt BIGINT NOT NULL DEFAULT 0,
  XVGamnt BIGINT NOT NULL DEFAULT 0,
  XVSamnt BIGINT NOT NULL DEFAULT 0,
  YFIamnt BIGINT NOT NULL DEFAULT 0,
  YFIIamnt BIGINT NOT NULL DEFAULT 0,
  ZECamnt BIGINT NOT NULL DEFAULT 0,
  ZILamnt BIGINT NOT NULL DEFAULT 0,
  ZRXamnt BIGINT NOT NULL DEFAULT 0,

);"""

class Database:
    """A database interface for the bot to connect to Postgres."""

    def __init__(self):
        self.pool = None

    async def setup(self):
        self.pool = await create_pool(dsn=getenv("DATABASE_URL"))
        await self.execute(CREATE)

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

    async def fetchrow(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def create_user(self, id: int):
        return await self.fetchrow("INSERT INTO Users (id) VALUES ($1) RETURNING *;", id)
    
    async def update_user_balance(self, id: int, xp: int):
        await self.execute("UPDATE Users SET balance = balance + $1 WHERE id = $2;", xp, id)

    async def get_coin_leaderboard(self):
        return await self.fetch("SELECT * FROM Users ORDER BY balance DESC LIMIT 15;")
        
    async def get_user(self, id: int):
        user =  await self.fetchrow("SELECT * FROM Users WHERE id = $1;", id)
        if user:
            return user
        return await self.create_user(id)