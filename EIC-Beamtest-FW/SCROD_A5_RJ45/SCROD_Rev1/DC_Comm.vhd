----------------------------------------------------------------------------------
-- Company: University of Hawaii Instrumentation Development Lab
-- Engineer: Nathan Park
-- 
-- Create Date:    19:23:18 04/12/2019 
-- Design Name: 
-- Module Name:    DC_Comm - Behaviorial 
-- Project Name: HODOSCOPE/Hawaii Muon Beamline
-- Target Devices: Spartan6 xc6slx150
-- Tool versions: 
-- Description: Interfaces SCROD with Daughtercards. Has one QBLink module per DC. Does global 
--              trigger logic. Specifically for HODOSCOPE,   
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use work.all;
use work.BMD_definitions.all; 
use work.UtilityPkg.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;
use ieee.std_logic_unsigned.all;
-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity DC_Comm is
	Generic ( num_DC : integer := 3); --highest index in DC signal vectors: (# of DCs) - 1  
    Port ( DATA_CLK : in  sl;
           RX : in  slv(num_DC downto 0);
           TX : out  slv(num_DC downto 0);
           DC_CMD : in  slv (31 downto 0); 
           CMD_VALID : in  slv( num_DC downto 0);
           RESP_REQ : in slv(num_DC downto 0);
			  DC_RESPONSES : out  Word32Array(num_DC downto 0); --be able to read received words from all DCs
			 	--to be added: WAVE_WD : out slv(31 downto 0);
				--             and WaveValid
				--to be added: TRIG : slv(31 downto 0);
				--            and TrigValid
           RESP_VALID : out  slv(num_DC downto 0);
			  QB_RST : in slv(num_DC downto 0);
			  TrigLogicRst : in sl;
			  SERIAL_CLK_LCK : out slv(num_DC downto 0);
			  TRIG_LINK_SYNC : out slv(num_DC downto 0);
			  Event_Trig : out sl --global event trigger 
			  );
end DC_Comm;

architecture Behaviorial of DC_Comm is
signal tx_dc : slv(num_DC downto 0):= (others => '0');
signal rx_dc : slv(num_DC downto 0);
signal dc_dataValid : slv(num_DC downto 0):= (others => '0');
signal rd_req : slv(num_DC downto 0):= (others => '0');
signal dc_data : Word32Array(num_DC downto 0);
signal trgLinkSync :slv(num_DC downto 0):= (others => '0');
signal serialClkLck : slv(num_DC downto 0):= (others => '0');
signal TrigFlag : slv(num_DC downto 0) := (others => '0');
begin
TX <= tx_dc;
rx_dc <= RX;
DC_RESPONSES <= dc_data; --after register program feature, if statement will read HEADER word: dc_data will either feed DC_RESPONSE or WAVE_WD OR TRIG
RESP_VALID <= dc_dataValid; 
rd_req <= RESP_REQ;  
TRIG_LINK_SYNC <= trgLinkSync;
SERIAL_CLK_LCK <= serialClkLck;

Gen_QBLink : FOR I in num_DC downto 0 GENERATE 
DC_Interface : entity work.QBLink                                                     
PORT MAP( 
			 sstClk => DATA_CLK,
			 rst => QB_RST(I),
			 rawSerialOut => tx_dc(I),
			 rawSerialIn => rx_dc(I),
			 localWordIn => DC_CMD, 
			 localWordInValid => CMD_VALID(I),
			 localWordOut => dc_data(I),
			 localWordOutValid => dc_dataValid(I),
			 localWordOutReq => rd_req(I),
			 trgLinkSynced => trgLinkSync(I),
			 serialClkLocked => serialClkLck(I)
			 );
end GENERATE Gen_QBLink;

TriggerLogic : process(dc_data, TrigFlag)
begin
	FOR  L in num_DC DOWNTO 0 loop 
		IF dc_data(L)(7 downto 5) = "111" THEN --If output word contains trigger data marker
			TrigFlag(L) <= '1'; --DC L is triggered.
		ELSE
			TrigFlag(L) <= '0'; --DC L is not triggered.
		END IF;
	END LOOP;
	
	IF TrigFlag = "1111" THEN -- AND trigger flags (hardcoded for HODOSCOPE)
		Event_Trig <= '1';
		
	ELSIF TrigLogicRst = '1' THEN
		Event_Trig <= '0';
	
	ELSE
		Event_Trig <= '0';
	END IF;
end process;

end Behaviorial;
