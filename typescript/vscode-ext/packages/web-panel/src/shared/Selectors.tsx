import { VSCodeDropdown, VSCodeLink, VSCodeOption } from '@vscode/webview-ui-toolkit/react'
import { useSelections } from './hooks'
import { useContext, useState } from 'react'
import { ASTContext } from './ASTProvider'
import { vscode } from '@/utils/vscode'
import Link from './Link'
import TypeComponent from './TypeComponent'
import { ProjectToggle } from './ProjectPanel'
import { Command, CommandInput, CommandEmpty, CommandGroup, CommandItem, CommandList } from '@/components/ui/command'
import { Popover, PopoverTrigger, PopoverContent } from '@/components/ui/popover'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import { ChevronsUpDown, Check } from 'lucide-react'
import SearchBarWithSelector from '@/lib/searchbar'

const FunctionDropdown: React.FC = () => {
  const [open, setOpen] = useState(false)
  const {
    db: { functions },
    setSelection,
  } = useContext(ASTContext)

  const { func } = useSelections()
  const value = func?.name.value;

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant='ghost'
          aria-expanded={open}
          className="w-[250px] sm:w-[450px] justify-between flex hover:bg-primary/90 hover:text-foreground"
        >
          <span className="min-w-[200px] sm:min-w-[400px] truncate w-full text-left">{value ?? "Select a function..."}</span>
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-1/3 min-w-[400px] p-0">
        <SearchBarWithSelector
          options={functions.map((func) => ({ value: func.name.value }))}
          onChange={(value) => {
            setSelection(undefined, value, undefined, undefined, undefined)
            setOpen(false)
          }}
        />
      </PopoverContent>
    </Popover>
  )

}

export const FunctionSelector: React.FC = () => {
  const { func } = useSelections()

  return (
    <div className="flex flex-col items-start gap-1">
      <div className="flex flex-row items-center gap-1">
        <ProjectToggle />

        <FunctionDropdown />
        {/* <span className="font-light">Function</span>
        <VSCodeDropdown
          value={func?.name.value ?? '<not-picked>'}
          onChange={(event) =>
            setSelection(
              undefined,
              (event as React.FormEvent<HTMLSelectElement>).currentTarget.value,
              undefined,
              undefined,
              undefined,
            )
          }
        >
          {function_names.map((func) => (
            <VSCodeOption key={func} value={func}>
              {func}
            </VSCodeOption>
          ))}
        </VSCodeDropdown> */}
      </div>
      {func && (
        <div className="flex flex-row items-center gap-0 text-xs">
          <span className='text-muted-foreground pr-1'>Fn signature</span>
          (
          {func.input.arg_type === 'positional' ? (
            <div className="flex flex-row gap-1">
              arg: <TypeComponent typeString={func.input.type} />
            </div>
          ) : (
            <div className="flex flex-row gap-1">
              {func.input.values.map((v) => (
                <div key={v.name.value}>
                  {v.name.value}: <TypeComponent typeString={v.type} />,
                </div>
              ))}
            </div>
          )}
          ) {'→'} {func.output.arg_type === 'positional' && <TypeComponent typeString={func.output.type} />}
        </div>
      )}
    </div>
  )
}

export const TestCaseSelector: React.FC = () => {
  const PLACEHOLDER = '<new>'
  const { setSelection } = useContext(ASTContext)
  const { func, test_case: { name } = {} } = useSelections()
  const test_cases = func?.test_cases.map((cases) => cases.name.value) ?? []

  if (!func) return null

  return (
    <>
      <VSCodeDropdown
        value={name?.value ?? PLACEHOLDER}
        onChange={(event) => {
          let value = (event as React.FormEvent<HTMLSelectElement>).currentTarget.value
          setSelection(undefined, undefined, undefined, value, undefined)
        }}
      >
        {test_cases.map((cases, index) => (
          <VSCodeOption key={index} value={cases}>
            {cases}
          </VSCodeOption>
        ))}
        <VSCodeOption value={PLACEHOLDER}>{PLACEHOLDER}</VSCodeOption>
      </VSCodeDropdown>
      {name && <Link item={name} display="Open File" />}
    </>
  )
}
